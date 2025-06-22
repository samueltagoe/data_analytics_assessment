
# 📊 Term Deposit Subscription Prediction – Final Report

## 🧭 Objective
Predict whether a client will subscribe to a term deposit based on historical bank marketing campaign data.

---

## 📦 Dataset
- **Source:** `bank-additional-full.csv`
- **Records:** 41,188
- **Features:** 20 inputs + 1 target (`y`)
- **Target Class Distribution:**
  - No: 88.7%
  - Yes: 11.3%

---

## 1. Exploratory Data Analysis (EDA)
- No missing values detected.
- Feature `duration` was removed due to data leakage concerns.
- Class imbalance identified (significant majority of "no").

---

## 2. Feature Engineering
- `contacted_before` created from `pdays` (1 = previously contacted).
- One-hot encoding applied to categorical features.
- Final feature count: **53**

---

## 3. Model Training
- **Algorithm:** Random Forest
- **Train/Test Split:** 80/20 (stratified)
- **Class Imbalance Strategy:** `class_weight='balanced'`

---

## 4. Model Evaluation

| Metric     | Score   |
|------------|---------|
| Accuracy   | 0.896   |
| Precision  | 0.576   |
| Recall     | 0.294   |
| F1 Score   | 0.389   |
| ROC AUC    | 0.776   |

> Model is accurate and slightly recall-optimized, though further improvement in identifying 'yes' class may require oversampling or different thresholds.

---

## 5. Top Predictive Features

- `euribor3m`, `nr.employed`, `emp.var.rate`, `cons.price.idx`, `poutcome_success`
- `contact_cellular`, `education_university.degree`, `age`, `contacted_before`
- Seasonal features (`month_mar`, `month_oct`)

---

## 6. Recommendations

- Focus marketing on clients with **successful past engagement**.
- Target **educated** and **older clients**.
- Time campaigns around **economic indicators** and **productive months**.
- Use **mobile outreach** where possible.

---

## 🔚 Deliverables

- `term_deposit_rf_model.joblib`: Trained prediction model
- Full feature-engineered dataset & processing code
