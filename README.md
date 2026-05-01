# FinRisk AI – Credit Intelligence System

### End-to-End Credit Risk Assessment, Simulation and Decision Platform

---

![Python](https://img.shields.io/badge/Python-3.9-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red)
![ML](https://img.shields.io/badge/MachineLearning-Enabled-green)
![Status](https://img.shields.io/badge/Status-Active-success)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

---

## Live Demo

Access the deployed application:
https://finrisk-intelligence.streamlit.app

---

## Support the Project

If you find this project useful, consider giving it a star.

---

## Project Preview

Add screenshots here:

* Dashboard
* Risk Analysis
* Simulator
* Excel Report

---

## Table of Contents

* Overview
* Why This Project Matters
* Features
* Architecture Diagram
* System Architecture
* How It Works
* Input Data Description
* Feature Engineering
* Machine Learning Model
* Decision Engine
* Scenario Simulator
* Optimization Engine
* Dashboard
* Report Generation
* Key Outputs
* Model Performance
* Explainability
* Tech Stack
* Project Structure
* Installation
* Usage
* Deployment
* Performance
* Limitations
* Future Improvements
* Acknowledgment
* Author

---

## Overview

FinRisk AI is a production-inspired credit risk intelligence system that simulates how banks and fintech platforms evaluate loan applicants using machine learning, financial metrics, and decision rules.

It provides real-time prediction, explainability, simulation, and professional reporting.

---

## Why This Project Matters

This project demonstrates:

* Real-world credit risk modeling
* End-to-end system design
* Financial domain understanding
* Explainable AI
* Production-grade dashboard

It bridges academic ML and real fintech systems.

---

## Features

* Credit Risk Prediction (Probability of Default)
* Credit Score Generation (300–900 scale)
* Decision Engine (Approve / Review / Reject)
* Explainable AI (Feature Importance)
* Scenario Simulation (What-if analysis)
* Loan Optimization Engine
* Power BI-style Interactive Dashboard
* Bank-level Excel Report Generation

---

## Architecture Diagram

<p align="center">
  <img src="./assets/architecture.png" width="90%">
</p>


---

## System Architecture

User Input → Feature Engineering → ML Model → Decision Engine → Dashboard → Report

---

## How It Works

1. User inputs applicant data
2. System processes and validates inputs
3. Feature engineering computes financial indicators
4. ML model predicts default probability
5. Decision engine applies business rules
6. Dashboard displays insights
7. Excel report is generated

---

## Input Data Description (Simple Explanation for Everyone)

This section explains each input field in simple terms so even someone without financial knowledge can understand how risk is evaluated.

---

### 1. Age

Represents the applicant’s age in years.

Why it matters:
- Very young applicants may have limited financial history
- Very old applicants may have repayment risks depending on income stability
- Middle age is generally considered stable

---

### 2. Income

Monthly income of the applicant.

Why it matters:
- Higher income → better repayment ability
- Lower income → higher risk

Example:
If income is ₹1,20,000/month, the person can handle higher EMIs safely.

---

### 3. Loan Amount

Total amount the applicant wants to borrow.

Why it matters:
- Larger loans increase financial burden
- Smaller loans are easier to repay

---

### 4. Loan Tenure (Months)

Duration of the loan in months.

Why it matters:
- Longer tenure → lower monthly EMI but longer commitment
- Shorter tenure → higher EMI but faster repayment

---

### 5. Avg DPD (Days Past Due)

Average number of days the applicant delayed payments in the past.

Why it matters:
- Indicates repayment discipline
- Higher DPD = poor repayment behavior

Example:
- 0–5 days → Good
- 20+ days → Risky

---

### 6. Delinquency Ratio (%)

Percentage of past payments that were delayed.

Why it matters:
- Shows how often the applicant misses payments
- Higher percentage = frequent payment issues

Example:
- 5% → Very good
- 30% → Risky borrower

---

### 7. Credit Utilization (%)

How much of available credit the applicant is currently using.

Formula:
Used Credit / Total Credit Limit

Why it matters:
- High utilization means financial stress

Example:
- 30% → Healthy
- 80% → High risk

---

### 8. Number of Open Accounts

Total active loans or credit accounts.

Why it matters:
- Too many loans → higher financial burden
- Too few → limited credit history

---

### 9. Residence Type

Type of housing:
- Owned
- Rented

Why it matters:
- Owned house → more financial stability
- Rented → slightly higher uncertainty

---

### 10. Loan Purpose

Reason for taking the loan.

Examples:
- Education
- Personal
- Home

Why it matters:
- Some purposes are considered safer (e.g., education, home)
- Others (personal loans) may be riskier

---

### 11. Loan Type

Type of loan:
- Secured (backed by asset)
- Unsecured (no collateral)

Why it matters:
- Secured loans → lower risk (bank can recover asset)
- Unsecured loans → higher risk

---

## Summary

All these inputs together help the system understand:

- Can the person repay the loan?
- How risky is the applicant?
- Should the loan be approved?

These are the same types of signals used in real banking systems.

## Feature Engineering

Derived features:

* Loan-to-Income Ratio
* EMI Calculation
* EMI Burden
* Debt-to-Income Ratio
* Risk Flags

---

## Machine Learning Model

Model: Logistic Regression

Reasons:

* Interpretable
* Fast
* Industry baseline

Outputs:

* Probability of Default
* Credit Score
* Risk Category

---

## Decision Engine

* Probability < 0.3 → Approve
* 0.3–0.6 → Review
* > 0.6 → Reject

Additional logic:

* High EMI burden increases risk
* High delinquency penalizes approval

---

## Scenario Simulator

Users can adjust:

* Income
* Loan Amount
* Tenure

Risk recalculates instantly.

---

## Optimization Engine

Optimizes:

* Loan Amount
* Tenure
* Risk Score

---

## Dashboard

* KPI Cards
* Risk Gauge
* Feature Importance Chart
* Filters
* Tabs
* Drill-down Analytics

---

## Report Generation

Excel report includes:

### Summary

* Probability
* Score
* Decision

### Inputs

* Full applicant data

### Importance

* Feature importance with chart

---

## Key Outputs

* Default Probability: ~66%
* Credit Score: ~500
* Risk Category: Medium Risk
* Loan-to-Income Ratio: ~2.13

---

## Model Performance

| Model               | Accuracy | Recall |
| ------------------- | -------- | ------ |
| Logistic Regression | 93%      | 94%    |
| Random Forest       | 91%      | 90%    |
| XGBoost             | 92%      | 91%    |

Logistic Regression chosen for interpretability and recall.

---

## Explainability

Uses SHAP:

* Identifies key drivers
* Explains predictions
* Supports transparency

---

## Tech Stack

Frontend:

* Streamlit

Backend:

* Python

ML:

* Scikit-learn

Data:

* Pandas, NumPy

Visualization:

* Plotly

Reporting:

* OpenPyXL

---

## Project Structure

```
finrisk-ai/
├── app/
│   └── app.py
├── assets/
├── models/
├── reports/
├── requirements.txt
└── README.md
```

---

## Installation

```bash
git clone https://github.com/jaswanthreddy/finrisk-ai.git
cd finrisk-ai
pip install -r requirements.txt
streamlit run app/app.py
```

---

## Usage

1. Enter applicant details
2. Click Analyze
3. View insights
4. Run simulation
5. Download report

---

## Deployment

Using Streamlit Cloud:

1. Push to GitHub
2. Connect repo
3. Set `app/app.py`
4. Deploy

---

## Performance

* Fast inference (<100ms)
* Real-time updates
* Lightweight

---

## Limitations

* No real credit bureau data
* Simplified assumptions
* Partial interest modeling

---

## Future Improvements

* Real datasets
* Advanced ML models
* Interest rate modeling
* API backend
* Authentication

---

## Acknowledgment

Inspired by real fintech and banking systems.

---

## Author

**Jaswanth Reddy Bandi**  
<p>
  <a href="https://www.linkedin.com/in/jaswanth-reddy-bandi-899525289/" target="_blank">LinkedIn</a> |
  <a href="https://github.com/jaswanthhreddy" target="_blank">GitHub</a>
</p>
