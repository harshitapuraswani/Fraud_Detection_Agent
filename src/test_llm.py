from llm_reasoning import explain_fraud

sample = {
    "amount": 4500,
    "country": "India",
    "device": "iPhone",
    "merchant_category": "Luxury",
    "failed_logins": 4,
    "new_device": 1
}

result = explain_fraud(
    sample,
    risk_score=80,
    prediction=1,
    reasons=[
        "High transaction amount",
        "Multiple failed login attempts",
        "New device login"
    ]
)

print(result)