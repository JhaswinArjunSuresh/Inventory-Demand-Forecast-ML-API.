import pandas as pd
import xgboost as xgb
import numpy as np
import pickle

class DemandForecaster:
    def __init__(self):
        with open("app/xgb_model.pkl", "rb") as f:
            self.model = pickle.load(f)

    def predict(self, recent_sales: list[int]) -> list[float]:
        # Here we take last 7 days sales as features
        X = np.array(recent_sales[-7:]).reshape(1, -1)
        preds = self.model.predict(X)
        return preds.tolist()

