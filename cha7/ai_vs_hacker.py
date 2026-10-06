ai_findings = [
    "Reentrancy vulnerability",
    "Missing access control",
    "Unchecked external call"
]

human_findings = [
    "Reentrancy vulnerability",
    "Missing access control",
    "Unchecked external call",
    "Anyone can use emergencyWithdraw",
    "Owner can be changed to an invalid address"
]

print("AI SECURITY ANALYSIS")
print("=" * 30)

for finding in ai_findings:
    print("[AI]", finding)

print("\nHUMAN SECURITY REVIEW")
print("=" * 30)

for finding in human_findings:
    print("[HUMAN]", finding)

missed = [finding for finding in human_findings if finding not in ai_findings]

print("\nAI MISSED:")
for finding in missed:
    print("-", finding)

print("\nTotal AI Findings:", len(ai_findings))
print("Total Human Findings:", len(human_findings))
print("Missed Findings:", len(missed))