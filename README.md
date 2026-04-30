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

## Input Data Description

### Demographics

* Age
* Residence Type

### Financial

* Income
* Loan Amount
* Loan Tenure

### Behavioral

* Average DPD
* Delinquency Ratio
* Credit Utilization
* Number of Open Accounts

### Loan Context

* Loan Type
* Loan Purpose

These reflect real-world banking risk signals.

---

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
