import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score
import joblib

# Load dataset
df = pd.read_csv("data/fraud_transactions.csv")

# -------------------------
# FIX: Handle datetime column
# -------------------------
df["transaction_time"] = pd.to_datetime(df["transaction_time"])

df["hour"] = df["transaction_time"].dt.hour
df["day"] = df["transaction_time"].dt.day
df["dayofweek"] = df["transaction_time"].dt.dayofweek

df = df.drop("transaction_time", axis=1)

# -------------------------
# Feature Engineering
# -------------------------
df["is_high_amount"] = df["amount"].apply(lambda x: 1 if x > 4000 else 0)

# Encode categorical features
df = pd.get_dummies(df, columns=["country", "device", "merchant_category"])

# Features & Label
X = df.drop(["fraud", "transaction_id"], axis=1)
y = df["fraud"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Model
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Evaluation
print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nReport:\n", classification_report(y_test, y_pred))

# Save model
joblib.dump(model, "models/fraud_model.pkl")

print("Model saved successfully!")