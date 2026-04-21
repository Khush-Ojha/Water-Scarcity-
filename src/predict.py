import os
import pickle
import numpy as np

# Get base project directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Correct paths
model_path = os.path.join(BASE_DIR, "models", "model.pkl")
scaler_path = os.path.join(BASE_DIR, "models", "scaler.pkl")

# Load files
model = pickle.load(open(model_path, "rb"))
scaler = pickle.load(open(scaler_path, "rb"))


def predict(consumption, groundwater, rainfall):
    
    risk_score = (
        0.4 * groundwater +
        0.3 * (1000 - rainfall) / 1000 +
        0.3 * (consumption / 100)
    )
    
    data = np.array([[consumption, groundwater, rainfall, risk_score]])
    data_scaled = scaler.transform(data)
    
    prediction = model.predict(data_scaled)
    
    return prediction[0]