
# Term Deposit Prediction API

This is a Flask API that predicts if a client will subscribe to a term deposit.

## 🛠 Setup Instructions

1. Upload this entire folder to a GitHub repo.
2. Go to [https://render.com](https://render.com)
3. Click **New > Web Service**
4. Connect your GitHub repo.
5. Set:
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `python app.py`

That's it! Render will give you a public URL to use.

## 🔄 API Usage

Send a `POST` request to `/predict` with a JSON body:
```json
{
  "job_admin.": 0,
  "education_university.degree": 1,
  ...
}
```

You’ll get back:
```json
{
  "prediction": 1,
  "probability": 0.73
}
```
