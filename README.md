# Telco Customer Churn Prediction

## 📌 Problem Statement
Customer churn is a critical challenge for telecom companies. This project predicts whether a customer is likely to churn based on demographic, subscription, and billing features.

---

## 📊 Dataset
Telco Customer Churn Dataset  
- 7,043 customer records  
- Mixed numerical and categorical features  
- Target variable: Churn (Yes/No)

---

## 🧹 Data Preprocessing
- Removed customerID (identifier)
- Converted TotalCharges to numeric
- Detected hidden missing values
- Median imputation applied
- One-Hot Encoding for categorical variables
- Standard Scaling for numerical features

---

## 🤖 Models Used
1. Logistic Regression  
2. Random Forest  
3. XGBoost  

---

## 📈 Evaluation Metrics
Models evaluated using:
- Accuracy
- Precision
- Recall
- F1-score

---

## 🏆 Best Model
Logistic Regression selected based on highest Recall and F1-score.

---

## 🧠 Model Explanation
Logistic Regression assigns coefficients to features:
- Positive coefficients → Increase churn probability
- Negative coefficients → Reduce churn probability

Key churn drivers:
- Month-to-month contracts
- Higher monthly charges

Retention factors:
- Longer tenure
- Long-term contracts

---

## 🚀 API Deployment
FastAPI-based REST API

### Endpoint
POST `/predict`

### Input
Customer data in JSON format

### Output
Prediction + churn probability

Example Response:
```json
{
  "prediction": 1,
  "probability_of_churn": 0.76
}
