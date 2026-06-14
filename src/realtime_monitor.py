import pandas as pd
import time

from fraud_agent import fraud_agent

# -----------------------------
# LOAD TRANSACTION DATA
# -----------------------------
df = pd.read_csv("data/fraud_transactions.csv")

print("\n🚀 Starting Real-Time Fraud Monitoring...\n")

# -----------------------------
# SIMULATE TRANSACTION STREAM
# -----------------------------
for index, row in df.head(10).iterrows():

    transaction = row.to_dict()

    # Run the fraud agent
    result = fraud_agent(transaction)

    # Print transaction details
    print("=" * 60)
    print(f"Transaction ID : {transaction['transaction_id']}")
    print(f"Customer ID    : {transaction['customer_id']}")
    print(f"Amount         : ${transaction['amount']}")
    print(f"Country        : {transaction['country']}")
    print(f"Merchant       : {transaction['merchant_category']}")

    # Agent output
    print("\n🤖 FRAUD AGENT RESULT")
    print(f"Decision      : {result['decision']}")
    print(f"Risk Score    : {result['risk_score']}")
    print(f"ML Prediction : {result['ml_prediction']}")

    print("\nRisk Indicators:")
    for reason in result["reasons"]:
        print(f"- {reason}")

    print("\nAI Explanation:")
    print(result["explanation"])

    # Alert if fraud detected
    if (
        result["decision"] == "FRAUD ALERT 🚨"
        or result["ml_prediction"] == 1
    ):
        print("\n🚨 ALERT: Transaction flagged for analyst review!")

    # Simulate real-time delay
    time.sleep(2)