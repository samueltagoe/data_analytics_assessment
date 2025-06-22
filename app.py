
from flask import Flask, request, jsonify
import joblib
import os
import requests
import numpy as np

MODEL_URL = "https://drive.google.com/uc?export=download&id=1efiTaTkgmkmIdPyvgGqdgafCqxM9--rK"
MODEL_PATH = "term_deposit_rf_render.joblib"

# Download model if not already available
if not os.path.exists(MODEL_PATH):
    print("Downloading model from Google Drive...")
    response = requests.get(MODEL_URL)
    with open(MODEL_PATH, "wb") as f:
        f.write(response.content)

# Load model
model = joblib.load(MODEL_PATH)

# Actual feature order from training
feature_order = [
    'age', 'duration', 'campaign', 'pdays', 'previous',
    'emp.var.rate', 'cons.price.idx', 'cons.conf.idx', 'euribor3m', 'nr.employed',
    'job_admin.', 'job_blue-collar', 'job_entrepreneur', 'job_housemaid', 'job_management',
    'job_retired', 'job_self-employed', 'job_services', 'job_student', 'job_technician',
    'job_unemployed', 'job_unknown',
    'marital_divorced', 'marital_married', 'marital_single', 'marital_unknown',
    'education_basic.4y', 'education_basic.6y', 'education_basic.9y', 'education_high.school',
    'education_illiterate', 'education_professional.course', 'education_university.degree',
    'education_unknown',
    'default_no', 'default_unknown', 'default_yes',
    'housing_no', 'housing_unknown', 'housing_yes',
    'loan_no', 'loan_unknown', 'loan_yes',
    'contact_cellular', 'contact_telephone',
    'month_apr', 'month_aug', 'month_dec', 'month_jul', 'month_jun',
    'month_mar', 'month_may', 'month_nov', 'month_oct', 'month_sep',
    'day_of_week_fri', 'day_of_week_mon', 'day_of_week_thu', 'day_of_week_tue', 'day_of_week_wed',
    'poutcome_failure', 'poutcome_nonexistent', 'poutcome_success'
]

app = Flask(__name__)

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    X_input = np.array([data.get(f, 0) for f in feature_order]).reshape(1, -1)
    prob = model.predict_proba(X_input)[0, 1]
    pred = int(prob > 0.5)
    return jsonify({"prediction": pred, "probability": prob})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
