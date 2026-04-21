import pickle
import numpy as np
import os
import pickle

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

model_path = os.path.join(BASE_DIR, "models", "model.pkl")
scaler_path = os.path.join(BASE_DIR, "models", "scaler.pkl")

model = pickle.load(open(model_path, "rb"))
scaler = pickle.load(open(scaler_path, "rb"))

def predict(consumption, groundwater, rainfall):
    
    # same risk formula
    risk_score = (
        0.4 * groundwater +
        0.3 * (1000 - rainfall) / 1000 +
        0.3 * (consumption / 100)
    )
    
    data = np.array([[consumption, groundwater, rainfall, risk_score]])
    data_scaled = scaler.transform(data)
    
    prediction = model.predict(data_scaled)
    
    return prediction[0]