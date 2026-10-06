import re

def read_file(filename):
    try:
        with open(filename, "r") as file:
            return file.read()

    except FileNotFoundError:
        print(f"[ERROR] File '{filename}' not found.")
        return ""

def detect_private_keys(text):

    pattern = r"0x[a-fA-F0-9]{64}"

    return re.findall(pattern, text)


def detect_wallet_addresses(text):

   
    pattern = r"0x[a-fA-F0-9]{40}"

    return re.findall(pattern, text)


def detect_secrets(text):

    secret_patterns = [
        r"api[_-]?key\s*=\s*[^\s]+",
        r"secret[_-]?key\s*=\s*[^\s]+",
        r"password\s*=\s*[^\s]+",
        r"token\s*=\s*[^\s]+"
    ]

    secrets = []

    for pattern in secret_patterns:
        matches = re.findall(pattern, text, re.IGNORECASE)
        secrets.extend(matches)

    return secrets




def calculate_risk(private_keys, wallets, secrets):

    score = 0

    
    score += len(private_keys) * 50

    score += len(wallets) * 10

    
    score += len(secrets) * 30

    score = min(score, 100)

    return score


def get_severity(score):

    if score >= 80:
        return "CRITICAL"

    elif score >= 60:
        return "HIGH"

    elif score >= 30:
        return "MEDIUM"

    else:
        return "LOW"




def mask_value(value):

    if len(value) <= 8:
        return "*" * len(value)

    return value[:4] + "*" * (len(value) - 8) + value[-4:]


def mask_secrets(text, private_keys, wallets, secrets):

    masked_text = text

    for value in private_keys:
        masked_text = masked_text.replace(
            value,
            mask_value(value)
        )

    for value in wallets:
        masked_text = masked_text.replace(
            value,
            mask_value(value)
        )

    for value in secrets:
        masked_text = masked_text.replace(
            value,
            mask_value(value)
        )

    return masked_text



def main():

    filename = "sample.txt"

    print("=" * 50)
    print("       BLOCKCHAIN SECURITY SCANNER")
    print("=" * 50)

   
    text = read_file(filename)

    if not text:
        return

  
    private_keys = detect_private_keys(text)
    wallets = detect_wallet_addresses(text)
    secrets = detect_secrets(text)

    
    risk_score = calculate_risk(
        private_keys,
        wallets,
        secrets
    )

    severity = get_severity(risk_score)

  
    print("\n[SCAN RESULTS]")

    print(f"Private Keys Found : {len(private_keys)}")
    print(f"Wallet Addresses   : {len(wallets)}")
    print(f"Other Secrets      : {len(secrets)}")

    print("\n[RISK ASSESSMENT]")

    print(f"Risk Score : {risk_score}/100")
    print(f"Severity   : {severity}")


    if risk_score > 0:

        print("\n SECURITY WARNING")
        print("Sensitive blockchain information has been exposed!")

    else:

        print("\n No obvious secrets detected.")

  
    if private_keys:

        print("\n[PRIVATE KEYS DETECTED]")

        for key in private_keys:
            print("  ", mask_value(key))

    if wallets:

        print("\n[WALLET ADDRESSES DETECTED]")

        for wallet in wallets:
            print("  ", mask_value(wallet))

    if secrets:

        print("\n[OTHER SECRETS DETECTED]")

        for secret in secrets:
            print("  ", mask_value(secret))


    print("\n[SAFE / MASKED FILE CONTENT]")

    masked_text = mask_secrets(
        text,
        private_keys,
        wallets,
        secrets
    )

    print(masked_text)

    print("=" * 50)




if __name__ == "__main__":
    main()