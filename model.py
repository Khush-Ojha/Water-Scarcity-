import pandas as pd
import matplotlib.pyplot as plt

from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.cluster import KMeans
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LinearRegression

# =====================
# LOAD DATA
# =====================
df = pd.read_csv("data/water.csv")

# =====================
# ENCODE TARGET
# =====================
le = LabelEncoder()
df["Water Scarcity Level"] = le.fit_transform(df["Water Scarcity Level"])

# =====================
# ADVANCED PART 1: RISK SCORE
# =====================
df["Risk Score"] = (
0.4 * df["Groundwater Depletion Rate (%)"] +
0.3 * (1000 - df["Rainfall Impact (mm)"]) / 1000 +
0.3 * df["Total Water Consumption (Billion m3)"] / 100
)

def risk_level(score):
    if score > 3:
        return 2   # High
    elif score > 2:
        return 1   # Moderate
    else:
        return 0   # Low

df["AI Risk Level"] = df["Risk Score"].apply(risk_level)

# =====================
# ADVANCED PART 2: CLUSTERING
# =====================
features = df[[
"Total Water Consumption (Billion m3)",
"Groundwater Depletion Rate (%)",
"Rainfall Impact (mm)"
]]

scaler = StandardScaler()
X_scaled = scaler.fit_transform(features)

kmeans = KMeans(n_clusters=3)
df["Cluster"] = kmeans.fit_predict(X_scaled)

# =====================
# ADVANCED PART 3: CLASSIFICATION
# =====================
X = df.drop(["Water Scarcity Level", "Country"], axis=1)
y = df["Water Scarcity Level"]

X_train, X_test, y_train, y_test = train_test_split(X, y)

clf = DecisionTreeClassifier()
clf.fit(X_train, y_train)

accuracy = clf.score(X_test, y_test)

# =====================
# FEATURE IMPORTANCE
# =====================
importance = clf.feature_importances_

plt.barh(X.columns, importance)
plt.title("Feature Importance")
plt.show()

# =====================
# ADVANCED PART 4: FORECASTING
# =====================
year_data = df.groupby("Year")["Total Water Consumption (Billion m3)"].mean().reset_index()

lr = LinearRegression()
lr.fit(year_data[["Year"]], year_data["Total Water Consumption (Billion m3)"])

future_years = list(range(2026, 2035))
future_preds = lr.predict([[y] for y in future_years])

plt.plot(year_data["Year"], year_data["Total Water Consumption (Billion m3)"])
plt.plot(future_years, future_preds)
plt.title("Future Water Consumption Prediction")
plt.show()

# =====================
# HIGH RISK COUNTRIES
# =====================
high_risk = df[
(df["Groundwater Depletion Rate (%)"] > 3) &
(df["Rainfall Impact (mm)"] < 800)
]["Country"].unique()

# =====================
# OUTPUT
# =====================
print("Model Accuracy:", accuracy)
print("Future Predictions:", future_preds)
print("High Risk Countries:", high_risk)