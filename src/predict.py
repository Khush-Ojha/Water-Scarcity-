import pickle
import numpy as np

model = pickle.load(open("models/model.pkl", "rb"))
scaler = pickle.load(open("models/scaler.pkl", "rb"))

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