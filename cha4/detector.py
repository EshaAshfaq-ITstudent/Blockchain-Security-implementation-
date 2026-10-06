tokens = [
    {
        "name": "Bitcoin",
        "symbol": "BTC",
        "contract": "0x1234567890abcdef1234567890abcdef12345678",
        "owner": "renounced",
        "website": "https://bitcoin.org"
    },
    {
        "name": "Bitcoin",
        "symbol": "BTC",
        "contract": "0x9999999999999999999999999999999999999999",
        "owner": "unknown",
        "website": "http://fake-bitcoin.com"
    },
    {
        "name": "SafeMoon",
        "symbol": "SAFEMOON",
        "contract": "0xabcdefabcdefabcdefabcdefabcdefabcdefabcd",
        "owner": "unknown",
        "website": "http://safemoon-fake.com"
    }
]

seen_names = set()

for token in tokens:
    risk = 0
    warnings = []

    if token["name"] in seen_names:
        risk += 30
        warnings.append("Duplicate token name")

    seen_names.add(token["name"])

    if token["owner"] == "unknown":
        risk += 30
        warnings.append("Unknown token owner")

    if not token["website"].startswith("https://"):
        risk += 20
        warnings.append("Suspicious website")

    if risk >= 60:
        status = "HIGH RISK"
    elif risk >= 30:
        status = "MEDIUM RISK"
    else:
        status = "LOW RISK"

    print("\nToken:", token["name"])
    print("Symbol:", token["symbol"])
    print("Contract:", token["contract"])
    print("Risk Score:", risk)
    print("Status:", status)

    if warnings:
        print("Warnings:")
        for warning in warnings:
            print("-", warning)
    else:
        print("Warnings: None")