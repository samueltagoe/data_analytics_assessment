
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

# Feature order from training (you MUST replace this with actual list)
feature_order = [/* insert your list of training features here */]

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
