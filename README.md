
# Term Deposit Prediction API

This is a Flask-based API to predict whether a client will subscribe to a term deposit.

## 🔧 How to Use (Render.com)

1. Go to [https://render.com](https://render.com)
2. Click **New + > Web Service**
3. Connect your GitHub repo (or upload files manually if zipped)
4. Select:
   - Runtime: Python 3
   - Start command: `python app.py`
   - Build command: `pip install -r requirements.txt`
5. Wait for deployment. You’ll get a live URL like `https://your-app.onrender.com`

## 📤 API Usage

**POST /predict**

Example input:
```json
{
  "age": 35,
  "campaign": 2,
  "pdays": 999,
  "previous": 0,
  "emp.var.rate": 1.1,
  "cons.price.idx": 93.994,
  "cons.conf.idx": -36.4,
  "euribor3m": 4.961,
  "nr.employed": 5228.1,
  "contacted_before": 0,
  ...
}
```

Response:
```json
{
  "prediction": 1,
  "probability": 0.73
}
```

