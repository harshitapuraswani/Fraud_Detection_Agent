import pandas as pd
import joblib

from risk_engine import calculate_risk
from llm_reasoning import explain_fraud

# -----------------------------
# LOAD MODEL + COLUMNS
# -----------------------------
model = joblib.load("models/fraud_model.pkl")
columns = joblib.load("models/model_columns.pkl")


# -----------------------------
# PREPROCESS FUNCTION
# -----------------------------
def preprocess(transaction):
    df = pd.DataFrame([transaction])
    df = pd.get_dummies(df)
    df = df.reindex(columns=columns, fill_value=0)
    return df


# -----------------------------
# FRAUD AGENT CORE
# -----------------------------
def fraud_agent(transaction):

    # Step 1: Risk Engine
    risk_score, reasons = calculate_risk(transaction)

    # Step 2: ML Prediction
    processed = preprocess(transaction)
    prediction = model.predict(processed)[0]

    # Step 3: LLM Reasoning
    explanation = explain_fraud(
        transaction,
        risk_score,
        prediction,
        reasons
    )

    # Step 4: Final Decision Logic
    if risk_score > 60 or prediction == 1:
        decision = "FRAUD ALERT 🚨"
    else:
        decision = "LEGIT TRANSACTION ✅"

    # Step 5: Output
    return {
        "decision": decision,
        "ml_prediction": int(prediction),
        "risk_score": risk_score,
        "reasons": reasons,
        "explanation": explanation
    }