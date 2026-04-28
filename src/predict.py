import joblib
import numpy as np
import pandas as pd
import logging

# ---------------- LOGGING ---------------- #
logging.basicConfig(
    filename="logs.txt",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# ---------------- LOAD MODEL ---------------- #
MODEL_PATH = "models/model.pkl"

model_data = joblib.load(MODEL_PATH)
model = model_data["model"]
scaler = model_data["scaler"]
features = model_data["features"]
cols_to_scale = model_data["cols_to_scale"]


# ---------------- PREPROCESS INPUT ---------------- #
def prepare_input(data: dict):
    """
    Convert raw input dict into model-ready dataframe
    """

    try:
        input_data = {
            'age': data['age'],
            'loan_tenure_months': data['loan_tenure_months'],
            'number_of_open_accounts': data['number_of_open_accounts'],
            'credit_utilization_ratio': data['credit_utilization_ratio'],
            'loan_to_income': data['loan_amount'] / data['income'] if data['income'] > 0 else 0,
            'delinquency_ratio': data['delinquency_ratio'],
            'avg_dpd_per_delinquency': data['avg_dpd_per_delinquency'],

            # One-hot encoding
            'residence_type_Owned': 1 if data['residence_type'] == 'Owned' else 0,
            'residence_type_Rented': 1 if data['residence_type'] == 'Rented' else 0,

            'loan_purpose_Education': 1 if data['loan_purpose'] == 'Education' else 0,
            'loan_purpose_Home': 1 if data['loan_purpose'] == 'Home' else 0,
            'loan_purpose_Personal': 1 if data['loan_purpose'] == 'Personal' else 0,

            'loan_type_Unsecured': 1 if data['loan_type'] == 'Unsecured' else 0,

            # Dummy/default features
            'number_of_dependants': 1,
            'years_at_current_address': 1,
            'zipcode': 1,
            'sanction_amount': 1,
            'processing_fee': 1,
            'gst': 1,
            'net_disbursement': 1,
            'principal_outstanding': 1,
            'bank_balance_at_application': 1,
            'number_of_closed_accounts': 1,
            'enquiry_count': 1
        }

        df = pd.DataFrame([input_data])

        # Scale required columns
        df[cols_to_scale] = scaler.transform(df[cols_to_scale])

        # Ensure correct feature order
        df = df[features]

        return df

    except Exception as e:
        logging.error(f"Error in prepare_input: {str(e)}")
        raise e


# ---------------- PREDICTION ---------------- #
def predict_risk(data: dict):
    """
    Main prediction function used by app
    """

    try:
        logging.info(f"Input received: {data}")

        # Basic validation (backend safety)
        if data["income"] <= 0:
            raise ValueError("Income must be greater than 0")
        if data["loan_amount"] <= 0:
            raise ValueError("Loan amount must be greater than 0")

        input_df = prepare_input(data)

        # Model probability
        prob = model.predict_proba(input_df)[0][1]

        # Credit score
        score = int(300 + (1 - prob) * 600)

        # Risk category
        if score < 500:
            rating = "High Risk"
        elif score < 650:
            rating = "Medium Risk"
        else:
            rating = "Low Risk"

        logging.info(f"Output: prob={prob}, score={score}, rating={rating}")

        return prob, score, rating

    except Exception as e:
        logging.error(f"Error in predict_risk: {str(e)}")
        raise e


# ---------------- OPTIONAL (INTERVIEW BONUS) ---------------- #
def get_model_input_features():
    """
    Returns feature names (useful for debugging / UI)
    """
    return features