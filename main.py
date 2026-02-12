from fastapi import FastAPI
import joblib
import pandas as pd

app = FastAPI()

model = joblib.load("best_model.pkl")

@app.get("/")
def home():
    return {"message": "Churn Prediction API Running"}

@app.post("/predict")
def predict(data: dict):
    input_df = pd.DataFrame([data])

    prediction = model.predict(input_df)[0]
    probability = model.predict_proba(input_df)[0][1]

    return {
        "prediction": int(prediction),
        "probability_of_churn": float(probability)
    }

