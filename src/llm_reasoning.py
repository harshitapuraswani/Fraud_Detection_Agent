def explain_fraud(transaction, risk_score, prediction, reasons):

    return f"""
Fraud Analysis Report

Prediction: {prediction}
Risk Score: {risk_score}

Reasons:
{", ".join(reasons)}

Recommendation:
Review transaction before approval.
"""