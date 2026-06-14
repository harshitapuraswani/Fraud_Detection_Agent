def explain_fraud(transaction, risk_score, prediction, reasons):

    if prediction == 1 or risk_score >= 50:
        recommendation = "Escalate transaction for fraud analyst review."
        summary = (
            "The transaction exhibits multiple suspicious indicators "
            "and has been flagged for additional investigation."
        )
    else:
        recommendation = "No immediate action required. Continue monitoring."
        summary = (
            "The transaction does not show significant fraud indicators "
            "and appears to be legitimate."
        )

    reason_text = ", ".join(reasons) if reasons else "No significant risk indicators detected."

    return f"""
Fraud Analysis Report

Prediction: {prediction}
Risk Score: {risk_score}

Summary:
{summary}

Reasons:
{reason_text}

Recommendation:
{recommendation}
"""