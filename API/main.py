from fastapi import FastAPI
import pandas as pd
import os

app = FastAPI(
    title="Neural Retail AI API",
    description="API for Neural Retail Dashboard",
    version="1.0"
)

@app.get("/")
def home():
    return {
        "message": "Neural Retail AI API is Running Successfully"
    }

@app.get("/forecast")
def forecast():

    file_path = "Data/Dashboard_Forecast.csv"

    if os.path.exists(file_path):

        df = pd.read_csv(file_path)

        return df.head(10).to_dict(orient="records")

    return {
        "error": "Dashboard_Forecast.csv not found"
    }


@app.get("/customers")
def customers():

    file_path = "Data/Customer_Analytics_Final.csv"

    if os.path.exists(file_path):

        df = pd.read_csv(file_path)

        return df.head(10).to_dict(orient="records")

    return {
        "error": "Customer_Analytics_Final.csv not found"
    }