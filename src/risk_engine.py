def calculate_risk(transaction):

    risk_score = 0
    reasons = []

    # High transaction amount
    if transaction["amount"] > 4000:
        risk_score += 40
        reasons.append(
            "High transaction amount"
        )

    # Multiple failed logins
    if transaction["failed_logins"] >= 3:
        risk_score += 30
        reasons.append(
            "Multiple failed login attempts"
        )

    # New device login
    if transaction["new_device"] == 1:
        risk_score += 20
        reasons.append(
            "Login from new device"
        )

    # Luxury merchant
    if (
        transaction["merchant_category"]
        == "Luxury"
    ):
        risk_score += 10
        reasons.append(
            "Luxury merchant purchase"
        )

    return risk_score, reasons