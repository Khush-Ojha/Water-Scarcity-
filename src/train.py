import pandas as pd
import pickle

from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

# =====================
# LOAD DATA
# =====================
df = pd.read_csv("../data/water.csv")

# =====================
# CREATE RISK SCORE (ADVANCED)
# =====================
df["Risk Score"] = (
0.4 * df["Groundwater Depletion Rate (%)"] +
0.3 * (1000 - df["Rainfall Impact (mm)"]) / 1000 +
0.3 * df["Total Water Consumption (Billion m3)"] / 100
)

# =====================
# ENCODE TARGET
# =====================
le = LabelEncoder()
df["Water Scarcity Level"] = le.fit_transform(df["Water Scarcity Level"])

# =====================
# FEATURES
# =====================
features = [
"Total Water Consumption (Billion m3)",
"Groundwater Depletion Rate (%)",
"Rainfall Impact (mm)",
"Risk Score"
]

X = df[features]
y = df["Water Scarcity Level"]

# =====================
# TRAIN MODEL
# =====================
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(X_scaled, y)

model = DecisionTreeClassifier()
model.fit(X_train, y_train)

accuracy = model.score(X_test, y_test)

# =====================
# SAVE MODEL + SCALER
# =====================
import os
os.makedirs("../models", exist_ok=True)

pickle.dump(model, open("../models/model.pkl", "wb"))
pickle.dump(scaler, open("../models/scaler.pkl", "wb"))

print("Model trained and saved!")
print("Accuracy:", accuracy)