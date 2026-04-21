import pickle
import numpy as np
import os

model_path = os.path.join(os.path.dirname(__file__), "..", "models", "model.pkl")
scaler_path = os.path.join(os.path.dirname(__file__), "..", "models", "scaler.pkl")

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