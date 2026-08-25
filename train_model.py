import pandas as pd
import numpy as np
from sklearn.ensemble import IsolationForest
import joblib

# generate training data
data = pd.DataFrame({
    "Power_Usage": np.random.normal(100, 20, 500),
    "Voltage": np.random.normal(220, 10, 500),
    "Frequency": np.random.normal(50, 0.5, 500)
})

model = IsolationForest(contamination=0.05)

model.fit(data)

joblib.dump(model, "model.pkl")

print("Model trained and saved")