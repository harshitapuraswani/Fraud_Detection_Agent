import streamlit as st
from fraud_agent import fraud_agent

st.set_page_config(page_title="Fraud Detection AI", layout="centered")

st.title("🚨 AI Fraud Detection System")
st.markdown("Enter transaction details to analyze fraud risk in real time.")

# -----------------------------
# INPUT FORM
# -----------------------------
transaction_id = st.text_input("Transaction ID", "TXN-001")
customer_id = st.text_input("Customer ID", "CUST-1001")
amount = st.number_input("Transaction Amount", min_value=0.0, value=500.0)
country = st.selectbox("Country", ["USA", "Canada", "India", "UK", "Germany"])
device = st.selectbox("Device", ["iPhone", "Android", "Windows", "MacBook"])
merchant = st.selectbox("Merchant Category", ["Grocery", "Electronics", "Travel", "Luxury"])
failed_logins = st.slider("Failed Login Attempts", 0, 5, 0)
new_device = st.radio("New Device?", [0, 1])

# -----------------------------
# BUILD TRANSACTION
# -----------------------------
transaction = {
    "transaction_id": transaction_id,
    "customer_id": customer_id,
    "amount": amount,
    "country": country,
    "device": device,
    "merchant_category": merchant,
    "failed_logins": failed_logins,
    "new_device": new_device
}

# -----------------------------
# RUN BUTTON
# -----------------------------
if st.button("Run Fraud Detection 🚨"):

    result = fraud_agent(transaction)

    st.subheader("📊 Result")

    st.write(f"**Decision:** {result['decision']}")
    st.write(f"**Risk Score:** {result['risk_score']}")
    st.write(f"**ML Prediction:** {result['ml_prediction']}")

    st.subheader("🔍 Reasons")
    st.write(result["reasons"])

    st.subheader("🧠 Explanation")
    st.text(result["explanation"])

    # ALERT UI
    if result["ml_prediction"] == 1 or result["risk_score"] > 50:
        st.error("🚨 FRAUD ALERT - Transaction flagged for review")
    else:
        st.success("✅ Transaction looks safe")