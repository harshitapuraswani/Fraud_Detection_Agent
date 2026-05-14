# synthetic_data_generator.py

from faker import Faker
import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

fake = Faker()

# -----------------------------
# CONFIG
# -----------------------------
NUM_TRANSACTIONS = 5000
FRAUD_PERCENTAGE = 0.08

countries = [
    "USA", "Canada", "India", "Brazil",
    "UK", "Germany", "Mexico", "Singapore"
]

devices = ["iPhone", "Android", "Windows", "MacBook", "Tablet"]

merchant_categories = [
    "Grocery", "Electronics", "Travel",
    "Restaurant", "Luxury", "Gaming"
]

# -----------------------------
# GENERATE DATA
# -----------------------------
data = []

for i in range(NUM_TRANSACTIONS):

    customer_id = random.randint(1000, 9999)

    amount = round(np.random.exponential(scale=120), 2)

    country = random.choice(countries)

    device = random.choice(devices)

    merchant = random.choice(merchant_categories)

    failed_logins = random.randint(0, 5)

    is_new_device = random.choice([0, 1])

    transaction_time = fake.date_time_between(
        start_date='-30d',
        end_date='now'
    )

    # -----------------------------
    # FRAUD LOGIC
    # -----------------------------
    fraud = 0

    fraud_conditions = [
        amount > 4000,
        failed_logins >= 3,
        is_new_device == 1 and country != "USA",
        merchant == "Luxury" and amount > 2000
    ]

    if sum(fraud_conditions) >= 2:
        fraud = 1

    # Add some random frauds
    if random.random() < FRAUD_PERCENTAGE:
        fraud = 1

    data.append({
        "transaction_id": i + 1,
        "customer_id": customer_id,
        "amount": amount,
        "country": country,
        "device": device,
        "merchant_category": merchant,
        "failed_logins": failed_logins,
        "new_device": is_new_device,
        "transaction_time": transaction_time,
        "fraud": fraud
    })

# -----------------------------
# CREATE DATAFRAME
# -----------------------------
df = pd.DataFrame(data)

# -----------------------------
# SAVE CSV
# -----------------------------
df.to_csv("fraud_transactions.csv", index=False)

print("Synthetic fraud dataset generated successfully!")
print(df.head())