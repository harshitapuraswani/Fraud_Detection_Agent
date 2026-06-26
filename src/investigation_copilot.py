def generate_investigation_report(transaction, result):
    """
    AI Fraud Investigation Copilot
    Converts raw fraud output into analyst-friendly explanation
    """

    reasons = result.get("reasons", [])
    risk_score = result.get("risk_score", 0)
    prediction = result.get("ml_prediction", 0)
    decision = result.get("decision", "UNKNOWN")

    # -----------------------------
    # 1. TRANSACTION SUMMARY
    # -----------------------------
    summary = (
        f"Transaction {transaction['transaction_id']} "
        f"for Customer {transaction['customer_id']} "
        f"was processed by the fraud detection system."
    )

    # -----------------------------
    # 2. RISK BREAKDOWN
    # -----------------------------
    if reasons:
        risk_breakdown = "\n".join([f"- {r}" for r in reasons])
    else:
        risk_breakdown = "- No significant risk indicators detected"

    # -----------------------------
    # 3. RISK INTERPRETATION
    # -----------------------------
    if risk_score >= 70 or prediction == 1:
        risk_level = "HIGH RISK"
        action = "🚨 Escalate to Fraud Investigation Team"
    elif risk_score >= 40:
        risk_level = "MEDIUM RISK"
        action = "⚠️ Manual review recommended"
    else:
        risk_level = "LOW RISK"
        action = "✅ Approve with monitoring"

    # -----------------------------
    # 4. FINAL REPORT
    # -----------------------------
    report = f"""
🧠 FRAUD INVESTIGATION COPILOT REPORT
----------------------------------------

📌 SUMMARY
{summary}

📊 DECISION: {decision}
📈 RISK SCORE: {risk_score}
🤖 ML PREDICTION: {prediction}
⚠️ RISK LEVEL: {risk_level}

🔍 KEY RISK INDICATORS
{risk_breakdown}

🚀 RECOMMENDED ACTION
{action}

----------------------------------------
"""

    return report