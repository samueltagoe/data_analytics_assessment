
from flask import Flask, request, jsonify
import joblib
import numpy as np

# Load model
model = joblib.load("term_deposit_rf_model.joblib")

# Feature order (must match training)
feature_order = ['age', 'campaign', 'pdays', 'previous', 'emp.var.rate', 'cons.price.idx', 'cons.conf.idx', 'euribor3m', 'nr.employed', 'contacted_before', 'job_blue-collar', 'job_entrepreneur', 'job_housemaid', 'job_management', 'job_retired', 'job_self-employed', 'job_services', 'job_student', 'job_technician', 'job_unemployed', 'job_unknown', 'marital_married', 'marital_single', 'marital_unknown', 'education_basic.6y', 'education_basic.9y', 'education_high.school', 'education_illiterate', 'education_professional.course', 'education_university.degree', 'education_unknown', 'default_unknown', 'default_yes', 'housing_unknown', 'housing_yes', 'loan_unknown', 'loan_yes', 'contact_telephone', 'month_aug', 'month_dec', 'month_jul', 'month_jun', 'month_mar', 'month_may', 'month_nov', 'month_oct', 'month_sep', 'day_of_week_mon', 'day_of_week_thu', 'day_of_week_tue', 'day_of_week_wed', 'poutcome_nonexistent', 'poutcome_success']

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    X_input = np.array([data.get(f, 0) for f in feature_order]).reshape(1, -1)
    probability = model.predict_proba(X_input)[0, 1]
    prediction = int(probability > 0.5)
    return jsonify({
        "prediction": prediction,
        "probability": probability
    })

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
