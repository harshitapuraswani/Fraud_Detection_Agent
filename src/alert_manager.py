import pandas as pd
import os
from datetime import datetime

ALERT_FILE = "data/fraud_alerts.csv"


def create_alert(transaction, result):
    os.makedirs("data", exist_ok=True)

    if os.path.exists(ALERT_FILE):
        alerts = pd.read_csv(ALERT_FILE)
    else:
        alerts = pd.DataFrame(columns=[
            "case_id",
            "transaction_id",
            "customer_id",
            "risk_score",
            "ml_prediction",
            "decision",
            "reasons",
            "status",
            "created_at"
        ])

    case_id = f"CASE-{len(alerts)+1:04d}"

    new_alert = {
        "case_id": case_id,
        "transaction_id": transaction["transaction_id"],
        "customer_id": transaction["customer_id"],
        "risk_score": result["risk_score"],
        "ml_prediction": result["ml_prediction"],
        "decision": result["decision"],
        "reasons": ", ".join(result["reasons"]),
        "status": "OPEN",
        "created_at": datetime.now()
    }

    alerts = pd.concat(
        [alerts, pd.DataFrame([new_alert])],
        ignore_index=True
    )

    alerts.to_csv(ALERT_FILE, index=False)

    return case_id

    def get_alert_queue():
     if not os.path.exists(ALERT_FILE):
        return pd.DataFrame()
    return pd.read_csv(ALERT_FILE)


def update_case_status(case_id, status):
    if not os.path.exists(ALERT_FILE):
        return

    alerts = pd.read_csv(ALERT_FILE)
    alerts.loc[
        alerts["case_id"] == case_id,
        "status"
    ] = status

    alerts.to_csv(ALERT_FILE, index=False)
