from urllib.parse import urlparse

urls = [
    "https://metamask.io",
    "http://metamask-wallet-security.com",
    "https://claim-free-eth.example.com",
    "http://wallet-connect-login.example.com"
]

crypto_keywords = ["crypto", "bitcoin", "ethereum", "eth", "token", "metamask"]
wallet_keywords = ["wallet", "connect", "metamask"]
login_keywords = ["login", "signin", "verify", "verification"]
urgency_words = ["urgent", "immediately", "now", "suspended"]
scam_words = ["free", "claim", "reward", "giveaway"]

for url in urls:
    risk = 0
    reasons = []
    domain = urlparse(url).netloc.lower()

    if url.startswith("http://"):
        risk += 20
        reasons.append("HTTP connection")

    if any(word in domain for word in crypto_keywords):
        risk += 10
        reasons.append("Crypto keyword")

    if any(word in domain for word in wallet_keywords):
        risk += 15
        reasons.append("Wallet keyword")

    if any(word in domain for word in login_keywords):
        risk += 20
        reasons.append("Login-related URL")

    if any(word in domain for word in urgency_words):
        risk += 15
        reasons.append("Urgency word")

    if any(word in domain for word in scam_words):
        risk += 20
        reasons.append("Free-token/scam language")

    if len(url) > 60:
        risk += 10
        reasons.append("Unusually long URL")

    risk = min(risk, 100)

    if risk >= 70:
        level = "CRITICAL"
    elif risk >= 40:
        level = "HIGH"
    elif risk >= 20:
        level = "MEDIUM"
    else:
        level = "LOW"

    print("\nURL:", url)
    print("Risk Score:", risk)
    print("Risk Level:", level)

    if reasons:
        print("Reasons:")
        for reason in reasons:
            print("-", reason)
    else:
        print("Reasons: None")