import shap
import joblib
import pandas as pd
import numpy as np

# Load model
MODEL_PATH = "models/model.pkl"

model_data = joblib.load(MODEL_PATH)
model = model_data["model"]
features = model_data["features"]

# ✅ Create background dataset (REQUIRED for new SHAP)
background = pd.DataFrame(
    np.zeros((1, len(features))),
    columns=features
)

# ✅ Correct explainer (new SHAP compatible)
explainer = shap.LinearExplainer(model, background)


def get_shap_values(input_df):
    """
    Generate SHAP values for given input
    """
    shap_values = explainer.shap_values(input_df)
    return shap_values


def get_feature_importance(shap_values, feature_names):
    """
    Compute feature importance from SHAP values
    """
    values = abs(shap_values).mean(axis=0)

    importance_df = pd.DataFrame({
        "feature": feature_names,
        "importance": values
    }).sort_values(by="importance", ascending=False)

    return importance_df