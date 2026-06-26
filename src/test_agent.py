from fraud_agent import fraud_agent
import pandas as pd

# Load sample transaction
df = pd.read_csv("data/fraud_transactions.csv")

fraud_samples = df[df["fraud"] == 1].sample(2)
legit_samples = df[df["fraud"] == 0].sample(2)

test_df = pd.concat([fraud_samples, legit_samples])

# Run agent
for i, row in test_df.iterrows():
    transaction = row.to_dict()
    result = fraud_agent(transaction)

print("\n===== FRAUD AGENT RESULT =====")

print(f"\nDecision: {result['decision']}")
print(f"Risk Score: {result['risk_score']}")
print(f"ML Prediction: {result['ml_prediction']}")

print("\nReasons:")
for reason in result["reasons"]:
    print(f"- {reason}")

print("\nExplanation:")
print(result["explanation"])

if "case_id" in result:
    print(f"\n📋 Case Created: {result['case_id']}")