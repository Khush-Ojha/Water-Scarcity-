import numpy as np

def predict(consumption, groundwater, rainfall):
    
    risk_score = (
        0.4 * groundwater +
        0.3 * (1000 - rainfall) / 1000 +
        0.3 * (consumption / 100)
    )

    if risk_score > 3:
        return 2
    elif risk_score > 2:
        return 1
    else:
        return 0