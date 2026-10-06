import re

def read_transactions(filename):

    transactions = []

    try:

        with open(filename, "r") as file:

            for line in file:

                line = line.strip()

                if not line:
                    continue

                transactions.append(line)

    except FileNotFoundError:

        print(f"[ERROR] File '{filename}' not found.")

    return transactions



def parse_transaction(line):

    parts = [part.strip() for part in line.split("|")]

    if len(parts) != 4:
        return None

    tx_id = parts[0]
    sender = parts[1]
    receiver = parts[2]


    amount_match = re.search(r"(\d+(?:\.\d+)?)\s*ETH", parts[3])

    if not amount_match:
        return None

    amount = float(amount_match.group(1))

    return {
        "id": tx_id,
        "sender": sender,
        "receiver": receiver,
        "amount": amount
    }



def parse_all_transactions(lines):

    transactions = []

    for line in lines:

        transaction = parse_transaction(line)

        if transaction:
            transactions.append(transaction)

    return transactions



def find_suspicious_wallets(transactions):

    suspicious_wallets = {
        "ScamWallet",
        "Mixer"
    }

    found = set()

    for tx in transactions:

        if tx["sender"] in suspicious_wallets:
            found.add(tx["sender"])

        if tx["receiver"] in suspicious_wallets:
            found.add(tx["receiver"])

    return found




def find_large_transfers(transactions, threshold=10):

    large_transactions = []

    for tx in transactions:

        if tx["amount"] >= threshold:

            large_transactions.append(tx)

    return large_transactions




def calculate_transaction_risk(
    suspicious_wallets,
    large_transactions,
    transactions
):

    score = 0
    reasons = []

    
    if suspicious_wallets:

        score += 40
        reasons.append(
            "Connected to suspicious wallet"
        )

   
    if large_transactions:

        score += 30
        reasons.append(
            "Large transaction detected"
        )


    mixer_found = False

    for tx in transactions:

        if (
            tx["sender"] == "Mixer"
            or tx["receiver"] == "Mixer"
        ):

            mixer_found = True

    if mixer_found:

        score += 30

        reasons.append(
            "Funds transferred to mixer"
        )

    score = min(score, 100)

    return score, reasons



def get_severity(score):

    if score >= 80:
        return "CRITICAL"

    elif score >= 60:
        return "HIGH"

    elif score >= 30:
        return "MEDIUM"

    return "LOW"


def display_transactions(transactions):

    print("\n[TRANSACTION DATA]")

    for tx in transactions:

        print(
            f"{tx['id']} | "
            f"{tx['sender']} -> "
            f"{tx['receiver']} | "
            f"{tx['amount']} ETH"
        )



def main():

    print("=" * 60)

    print(
        "       BLOCKCHAIN TRANSACTION DETECTIVE"
    )

    print("=" * 60)

    
    lines = read_transactions(
        "transactions.txt"
    )

    
    transactions = parse_all_transactions(lines)

    if not transactions:

        print("[ERROR] No valid transactions found.")

        return

   
    display_transactions(transactions)

    suspicious_wallets = find_suspicious_wallets(
        transactions
    )


    large_transactions = find_large_transfers(
        transactions
    )

  
    risk_score, reasons = calculate_transaction_risk(
        suspicious_wallets,
        large_transactions,
        transactions
    )

    severity = get_severity(risk_score)


    print("\n[INVESTIGATION RESULTS]")

    print(
        f"Suspicious Wallets: "
        f"{len(suspicious_wallets)}"
    )

    for wallet in suspicious_wallets:

        print(f"  - {wallet}")

    print(
        f"\nLarge Transactions: "
        f"{len(large_transactions)}"
    )

    for tx in large_transactions:

        print(
            f"  - {tx['id']}: "
            f"{tx['amount']} ETH"
        )



    print("\n[RISK ASSESSMENT]")

    print(
        f"Risk Score : {risk_score}/100"
    )

    print(
        f"Severity   : {severity}"
    )


    if reasons:

        print("\n[REASONS]")

        for reason in reasons:

            print(f"- {reason}")

  

    if risk_score >= 80:

        print("\n SUSPICIOUS TRANSACTION")

        print(
            "Immediate investigation recommended."
        )

    elif risk_score >= 60:

        print("\n HIGH-RISK TRANSACTION")

    elif risk_score >= 30:

        print("\n MEDIUM-RISK TRANSACTION")

    else:

        print("\n No major suspicious activity detected.")

    print("=" * 60)

def create_transaction_graph(transactions):

    import networkx as nx
    import matplotlib.pyplot as plt

    graph = nx.DiGraph()

    for tx in transactions:

        graph.add_edge(
            tx["sender"],
            tx["receiver"],
            amount=tx["amount"]
        )

    positions = nx.spring_layout(graph)

    nx.draw(
        graph,
        positions,
        with_labels=True,
        node_size=2500,
        arrows=True
    )

    edge_labels = {}

    for tx in transactions:

        edge_labels[
            (tx["sender"], tx["receiver"])
        ] = f"{tx['amount']} ETH"

    nx.draw_networkx_edge_labels(
        graph,
        positions,
        edge_labels=edge_labels
    )

    plt.title(
        "Blockchain Transaction Flow"
    )

    plt.show()

if __name__ == "__main__":

    main()

