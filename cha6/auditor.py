issues = [
    {
        "name": "Reentrancy",
        "severity": "HIGH",
        "description": "External call is made before balance update."
    },
    {
        "name": "Missing access control",
        "severity": "HIGH",
        "description": "Anyone can change the contract owner."
    },
    {
        "name": "Unchecked external call",
        "severity": "MEDIUM",
        "description": "The return value of target.call is not checked."
    },
    {
        "name": "Unsafe withdrawal",
        "severity": "HIGH",
        "description": "Anyone can call emergencyWithdraw."
    },
    {
        "name": "Missing validation",
        "severity": "MEDIUM",
        "description": "newOwner is not checked before changing ownership."
    }
]

print("SMART CONTRACT SECURITY AUDIT")
print("=" * 35)

for i, issue in enumerate(issues, 1):
    print(f"\n{i}. {issue['name']}")
    print("Severity:", issue["severity"])
    print("Description:", issue["description"])

print("\nTotal Issues:", len(issues))