# Fraud_Detection_Agent

# 🤖 AI Fraud Detection Agent

An end-to-end AI-powered fraud detection system that combines Machine Learning, rule-based risk scoring, and an interactive Streamlit dashboard to simulate how financial institutions analyze potentially fraudulent transactions.

---

## 🚀 Project Overview

This project was built as part of my **30-Day AI Agent Challenge** to explore how AI can be used to detect and analyze fraudulent financial transactions.

Instead of focusing only on model training, this project demonstrates how multiple AI components can work together to create a usable fraud detection application.

The system allows users to:

* Analyze financial transactions in real time
* Predict fraudulent transactions using Machine Learning
* Apply business rules for additional risk scoring
* Generate human-readable fraud explanations
* Interact with the system through a Streamlit web application

---

# 🏗️ System Architecture

```text
                User Input
                     │
                     ▼
         Streamlit Web Application
                     │
                     ▼
          Fraud Detection Agent
                     │
        ┌────────────┴────────────┐
        ▼                         ▼
Machine Learning Model     Rule-Based Engine
        │                         │
        └────────────┬────────────┘
                     ▼
             Risk Assessment
                     │
                     ▼
            Fraud Explanation
                     │
                     ▼
            Final Fraud Decision
```

---

# ✨ Features

### 📊 Synthetic Fraud Data Generation

* Generates realistic financial transactions
* Simulates fraud patterns
* Supports model training and testing

---

### 🤖 Machine Learning Fraud Detection

Uses Scikit-learn to classify transactions as:

* Fraud
* Legitimate

Includes:

* Feature engineering
* Model training
* Model serialization with Joblib

---

### ⚠️ Rule-Based Risk Engine

Business rules evaluate additional fraud signals such as:

* High transaction amount
* New device login
* Multiple failed login attempts
* Suspicious merchant categories

Each rule contributes to an overall risk score.

---

### 🧠 Fraud Detection Agent

The agent orchestrates the complete workflow by:

* Receiving transaction details
* Running ML prediction
* Applying business rules
* Calculating risk score
* Producing the final fraud decision

---

### 📱 Streamlit Dashboard

Interactive web interface where users can:

* Enter transaction details
* Run fraud analysis
* View prediction results
* See risk scores
* Understand why a transaction was flagged

---

# 📂 Project Structure

```text
Fraud_Detection_Agent/

│── data/
│     └── fraud_transactions.csv
│
│── models/
│     ├── fraud_model.pkl
│     └── model_columns.pkl
│
│── src/
│     ├── app.py
│     ├── fraud_agent.py
│     ├── train_model.py
│     ├── risk_engine.py
│     ├── llm_reasoning.py
│     ├── synthetic_data.py
│     ├── test_agent.py
│     └── view_alerts.py
│
├── requirements.txt
├── README.md
```

---

# ⚙️ Technologies Used

* Python
* Streamlit
* Scikit-learn
* Pandas
* NumPy
* Joblib

---

# 🚀 Installation

Clone the repository

```bash
git clone https://github.com/harshitapuraswani/Fraud_Detection_Agent.git
```

Move into the project

```bash
cd Fraud_Detection_Agent
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Train the Model

```bash
python src/train_model.py
```

---

# ▶️ Launch the Streamlit Application

```bash
streamlit run src/app.py
```

The application will open in your browser, where you can enter transaction details and run fraud analysis in real time.

---

# 📈 Sample Output

```text
Decision: FRAUD ALERT 🚨

Risk Score: 85

ML Prediction: 1

Reasons:
• High transaction amount
• New device login
• Multiple failed login attempts

Recommendation:
Escalate transaction for investigation.
```

---

# 🎥 Demo

*A demo video of the application is available on my LinkedIn.*

---

# 📚 Key Learnings

Throughout this project, I learned that building AI systems is about much more than training models.

Some of the biggest takeaways include:

* Data quality is critical.
* Machine learning and business rules complement each other.
* Explainability improves trust in AI systems.
* User experience is just as important as model accuracy.
* Building complete AI products requires orchestration, not just algorithms.

---

# 🔮 Future Improvements

* Real-time transaction streaming
* REST API integration
* Cloud deployment
* Database-backed alert management
* User authentication
* Explainable AI visualizations
* Multi-model fraud detection

---

# 👩‍💻 Author

**Harshita Puraswani**
If you found this project interesting, feel free to connect with me on LinkedIn or explore the repository.
