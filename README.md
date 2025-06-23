
# 🏦 Term Deposit Prediction Project

This repository contains the final submission for a predictive analytics project focused on bank marketing data.

---

## 🚀 Project Objective
The goal of this project is to develop a predictive machine learning model that determines whether a client will subscribe to a term deposit based on their profile and interaction history with the bank.

---

## 🧠 Problem Statement

In a highly competitive financial services industry, understanding customer behavior is key. This project aims to support the bank's direct marketing campaigns by building a model that predicts the likelihood of a client subscribing to a term deposit (`y = yes` or `no`). This helps the bank prioritize outreach efforts and optimize resource allocation.

---

## 🗂️ Dataset

The datasets provided for this project are based on real-world direct marketing campaigns conducted via phone calls.

  **Files:**
- `bank-additional.csv` – A 10% sample of the full dataset
- `bank-additional-full.csv` – The complete version with 41,188 rows and 20 features

**Key features include:**
- **Client details**: age, job, marital status, education
- **Banking history**: default status, housing/personal loan, account balance
- **Contact information**: contact type, duration, campaign frequency
- **Past interactions**: previous campaign outcomes
- **Target variable**: `y` – whether the client subscribed to a term deposit

---

## 🧰 Tools & Technologies

- **Language**: Python
- **Data Processing**: Pandas, NumPy
- **Visualization**: Matplotlib, Seaborn
- **Modeling**: Scikit-learn (Logistic Regression, Decision Trees, Random Forests)
- **Model Deployment**: Streamlit (optional)
- **Model Serialization**: Joblib

---

## ✅ Deliverables

- A trained machine learning model: `term_deposit_model.joblib`
- Clean, reproducible notebooks for:
  - Exploratory Data Analysis (EDA)
  - Feature Engineering
  - Model Training & Evaluation
- (Optional) A Streamlit-based interactive web app for making predictions
- This GitHub repository with all source code, model files, and documentation

---

## 📈 Model Overview

The final model uses features such as campaign duration, contact type, and client demographics to make predictions. It was evaluated using:
- Accuracy
- Precision
- Recall
- F1-Score
- ROC-AUC Score

These metrics help ensure the model is not only accurate but also robust in distinguishing potential subscribers from non-subscribers.
