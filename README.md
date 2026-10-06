# Web3 Security Wars

> A practical blockchain security project covering private-key exposure, transaction analysis, smart-contract vulnerabilities, phishing detection, token verification, security auditing, and AI-assisted security review.

## Table of Contents

- [About](#about)
- [Challenges](#challenges)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [How to Run](#how-to-run)
- [Security Concepts](#security-concepts)
- [Learning Outcomes](#learning-outcomes)
- [Disclaimer](#disclaimer)

## About

This project contains 7 practical blockchain and Web3 security challenges.

The goal is to understand how common blockchain security problems can be detected, analyzed, and mitigated using Python and Solidity.

## Challenges

| # | Challenge | Technology | Focus |
|---|---|---|---|
| 01 | 🔐 Private Key Guardian | Python | Secret & private-key detection |
| 02 | 🔎 Blockchain Transaction Detective | Python | Suspicious transaction analysis |
| 03 | 🔁 Reentrancy Attack Detector | Solidity + Hardhat | Smart-contract reentrancy |
| 04 | 🪙 Fake Token Detector | Python | Token verification |
| 05 | 🎣 Blockchain Phishing Detector | Python | Phishing & scam detection |
| 06 | 🛡️ Smart Contract Security Auditor | Python + Solidity | Vulnerability auditing |
| 07 | 🤖 AI vs Blockchain Hacker | Python + Solidity | AI security analysis |

<details>
<summary>🔐 Challenge 01 — Private Key Guardian</summary>

Detects potentially exposed:

- Private keys
- Wallet addresses
- API keys
- Other sensitive secrets

The scanner assigns a risk score from 0–100 and generates security warnings.

</details>

<details>
<summary>🔎 Challenge 02 — Blockchain Transaction Detective</summary>

Analyzes blockchain transaction data and detects:

- Suspicious wallets
- Unusually large transfers
- Transfers involving suspicious addresses
- High-risk transactions

The program generates a risk score and security alert.

</details>

<details>
<summary>🔁 Challenge 03 — Reentrancy Attack Detector</summary>

Demonstrates a vulnerable Solidity bank contract and a secure implementation.

The challenge covers:

- Reentrancy vulnerability
- External calls
- Checks-Effects-Interactions
- Secure withdrawal logic
- Reentrancy attack concept

The project uses Hardhat and Solidity for contract development and compilation.

</details>

<details>
<summary>🪙 Challenge 04 — Fake Token Detector</summary>

Checks token information for suspicious characteristics such as:

- Duplicate token names
- Unknown ownership
- Suspicious websites
- Unusual token metadata

A risk score and risk level are generated for each token.

</details>

<details>
<summary>🎣 Challenge 05 — Blockchain Phishing Detector</summary>

Analyzes URLs for phishing and scam indicators including:

- HTTP instead of HTTPS
- Crypto-related keywords
- Wallet-related keywords
- Login pages
- Urgency language
- Free-token/scam language
- Unusually long URLs

Each URL receives a risk score and risk level.

</details>

<details>
<summary>🛡️ Challenge 06 — Smart Contract Security Auditor</summary>

Performs a basic security audit of a Solidity smart contract.

The audit identifies issues including:

- Reentrancy
- Missing access control
- Unchecked external calls
- Unsafe withdrawal logic
- Missing validation

Each issue includes a severity level and description.

</details>

<details>
<summary>🤖 Challenge 07 — AI vs Blockchain Hacker</summary>

Compares an AI-generated security analysis with a human security review.

The human review identifies security issues that the initial AI analysis missed.

This demonstrates an important security principle:

> AI can assist security analysis, but security findings should still be manually validated.

</details>

## Tech Stack

### 🐍 Python

Used for:

- Security scanners
- Transaction analysis
- Token detection
- Phishing detection
- Smart-contract auditing
- AI vs human comparison

### ⛓️ Solidity

Used for:

- Vulnerable smart contracts
- Secure smart contracts
- Reentrancy demonstrations

### ⚒️ Hardhat

Used for:

- Solidity development
- Contract compilation
- Local blockchain development
- Smart-contract testing

## Project Structure

```text
blockchain/
│
├── cha1/
│   ├── scanner.py
│   └── sample.txt
│
├── cha2/
│   ├── detective.py
│   └── transactions.txt
│
├── cha3/
│   ├── contracts/
│   │   ├── VulnerableBank.sol
│   │   ├── SecureBank.sol
│   │   └── ReentrancyAttack.sol
│   ├── test/
│   │   └── Reentrancy.ts
│   ├── hardhat.config.ts
│   ├── package.json
│   └── ...
│
├── cha4/
│   └── detector.py
│
├── cha5/
│   └── phishing_detector.py
│
├── cha6/
│   ├── VulnerableContract.sol
│   └── auditor.py
│
├── cha7/
│   ├── VulnerableContract.sol
│   └── ai_vs_hacker.py
│
├── README.md
└── .gitignore
