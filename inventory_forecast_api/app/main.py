from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from .model import DemandForecaster

app = FastAPI()
forecaster = DemandForecaster()

class ForecastRequest(BaseModel):
    sku: str
    recent_sales: List[int]

@app.post("/forecast")
def forecast(request: ForecastRequest):
    prediction = forecaster.predict(request.recent_sales)
    return {"sku": request.sku, "forecast_next_7_days": prediction}

@app.get("/health")
def health():
    return {"status": "ok"}

