import numpy as np

def predict(consumption, groundwater, rainfall):
    
    # Risk score formula
    risk_score = (
        0.4 * groundwater +
        0.3 * (1000 - rainfall) / 1000 +
        0.3 * (consumption / 100)
    )

    # Simple classification logic
    if risk_score > 3:
        return 2   # High
    elif risk_score > 2:
        return 1   # Moderate
    else:
        return 0   # Low