import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__)))
from alert_manager import create_alert
import pandas as pd

transaction = {
    "transaction_id": "T123",
    "customer_id": "C456",
    "amount": 100.0
}

result = {
    "risk_score": 0.85,
    "ml_prediction": "fraud",
    "decision": "REVIEW",
    "reasons": ["high_amount", "velocity"]
}

case_id = create_alert(transaction, result)
print("Created case:", case_id)
print("--- alerts CSV ---")
print(pd.read_csv(os.path.join(os.getcwd(), "data", "fraud_alerts.csv")))
