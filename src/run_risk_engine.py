import pandas as pd

from risk_engine import calculate_risk

# Load dataset
df = pd.read_csv(
    "data/fraud_transactions.csv"
)

# Pick one sample transaction
sample_transaction = df.iloc[0].to_dict()

# Calculate risk
risk_score, reasons = calculate_risk(
    sample_transaction
)

# Print results
print("\nTransaction:")
print(sample_transaction)

print("\nRisk Score:")
print(risk_score)

print("\nFraud Indicators:")
for reason in reasons:
    print("-", reason)