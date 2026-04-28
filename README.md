# 💼 FinRisk AI – Credit Intelligence System

An end-to-end **production-style credit risk prediction platform** built using Machine Learning, Explainable AI (SHAP), and an interactive dashboard.

This system simulates how modern banks and fintech companies evaluate loan applicants using **data-driven risk scoring and explainability**.

---

## 🚀 Live Demo

👉 *(Add your deployed Streamlit link here)*

---

## 🎯 Project Overview

FinRisk AI predicts the **probability of loan default**, generates a **credit score (300–900)**, and provides **clear explanations** behind each decision using SHAP.

Unlike basic ML projects, this system focuses on:

* Real-world financial use case
* Explainable AI (not black-box predictions)
* Production-style UI and system design

---

## 🌟 Key Features

### 🔹 Core ML Capabilities

* Loan default prediction using Logistic Regression
* Credit score generation (300–900 scale)
* Risk classification (Low / Medium / High)

---

### 🔹 Explainable AI (SHAP)

* Feature importance visualization
* SHAP waterfall plots (individual prediction explanation)
* Human-readable decision insights

---

### 🔹 Advanced Dashboard UI

* KPI cards (Probability, Score, Risk)
* Risk gauge visualization
* Model comparison chart
* Interactive financial insights

---

### 🔹 Production-Level Features

* Input validation (prevents invalid predictions)
* Logging system (tracks predictions)
* Downloadable prediction report (CSV)
* Session state management

---

## 🏗️ Project Architecture

```
finrisk-ai/
│
├── app/
│   └── app.py                # Streamlit dashboard UI
│
├── src/
│   ├── predict.py           # ML prediction logic
│   ├── explain.py           # SHAP explainability
│
├── models/
│   └── model.pkl            # Trained ML model
│
├── notebooks/
│   └── ml_credit_risk_model.ipynb
│
├── .streamlit/
│   └── config.toml          # UI theme
│
├── requirements.txt
└── README.md
```

---

## 📊 Model Performance

| Model               | Accuracy | Recall  |
| ------------------- | -------- | ------- |
| Logistic Regression | **93%**  | **94%** |
| Random Forest       | ~91%     | ~90%    |
| XGBoost             | ~92%     | ~91%    |

👉 Logistic Regression chosen for:

* High recall (important in finance)
* Interpretability (regulatory requirement)

---

## 📊 Explainability (Why Prediction?)

The system uses **SHAP (SHapley Additive Explanations)** to:

* Identify top influencing features
* Visualize contribution of each feature
* Explain individual predictions clearly

---

## 📈 Example Dashboard Features

* Default probability visualization
* Credit score calculation
* Risk gauge (green → yellow → red)
* Feature importance chart
* SHAP waterfall plot
* Decision explanation panel

---

## 🛠️ Tech Stack

* Python
* Scikit-learn
* Pandas / NumPy
* SHAP (Explainable AI)
* Plotly (visualizations)
* Streamlit (UI)
* Joblib (model serialization)

---

## ⚙️ Installation & Setup

### 1. Clone Repository

```bash
git clone https://github.com/your-username/finrisk-ai
cd finrisk-ai
```

---

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 3. Run Application

```bash
streamlit run app/app.py
```

---

### 4. Open in Browser

```
http://localhost:8501
```

---

## 📋 How It Works

1. User enters financial details
2. Data is preprocessed (scaling + encoding)
3. Model predicts default probability
4. Credit score is calculated
5. SHAP explains the decision
6. Results displayed in dashboard

---

## ⚠️ Important Notes

* Model uses engineered features (loan-to-income, credit utilization, etc.)
* Some features are simulated (for demo purposes)
* Not intended for real financial decision-making

---

## 🚀 Future Improvements

* FastAPI backend (production API)
* Docker deployment
* Real-world dataset integration
* Model monitoring dashboard
* Ensemble models (LightGBM, CatBoost)

---

## 🧠 Key Learnings

* End-to-end ML system design
* Explainable AI implementation
* Production-style UI development
* Feature engineering for finance domain

---

## 👨‍💻 Author

**Bandi Jaswanth Reddy**

* GitHub: *(add your link)*
* LinkedIn: *(add your link)*

---

## ⭐ Support

If you found this project useful:

👉 Star ⭐ the repository
👉 Share feedback
👉 Fork and improve

---
