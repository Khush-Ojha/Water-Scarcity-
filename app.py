import streamlit as st
import pandas as pd
import sys
import os
import matplotlib.pyplot as plt
import seaborn as sns

# ML imports (keep here, not mid-code)
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# Fix import path
sys.path.append(os.path.abspath("src"))
from predict import predict

# Load data
df = pd.read_csv("data/water.csv")

# =====================
# TITLE
# =====================
st.title("🌍 AI Water Scarcity Analysis System")
st.write("AI system for analyzing and predicting global water scarcity.")

# =====================
# TREND
# =====================
st.subheader("📈 Global Water Consumption Trend")
trend = df.groupby("Year")["Total Water Consumption (Billion m3)"].mean()
st.line_chart(trend)

# =====================
# 🔥 CORRELATION HEATMAP (NEW)
# =====================
st.subheader("📊 Correlation Heatmap")

numeric_cols = df.select_dtypes(include=['float64', 'int64'])

fig_heat, ax_heat = plt.subplots()
sns.heatmap(numeric_cols.corr(), annot=True, cmap="coolwarm", ax=ax_heat)

st.pyplot(fig_heat)

# =====================
# RISK SCORE
# =====================
df["Risk Score"] = (
    0.4 * df["Groundwater Depletion Rate (%)"] +
    0.3 * (1000 - df["Rainfall Impact (mm)"]) / 1000 +
    0.3 * df["Total Water Consumption (Billion m3)"] / 100
)

# =====================
# TOP 10 COUNTRIES
# =====================
st.subheader("🏆 Top 10 High Risk Countries")

country_risk = df.groupby("Country")["Risk Score"].mean().reset_index()
top10 = country_risk.sort_values("Risk Score", ascending=False).head(10)

st.table(top10)

# =====================
# 🧠 K-MEANS CLUSTERING (NEW)
# =====================
st.subheader("🧠 Country Risk Clustering")

features = [
    "Total Water Consumption (Billion m3)",
    "Groundwater Depletion Rate (%)",
    "Rainfall Impact (mm)"
]

country_avg = df.groupby("Country")[features].mean()

scaler = StandardScaler()
X_scaled = scaler.fit_transform(country_avg)

kmeans = KMeans(n_clusters=4, random_state=42, n_init=10)
country_avg["Cluster"] = kmeans.fit_predict(X_scaled)

st.write(country_avg.head())

# =====================
# 📍 CLUSTER VISUALIZATION (IMPROVED)
# =====================
st.subheader("📍 Cluster Visualization")

fig2, ax2 = plt.subplots()

scatter = ax2.scatter(
    country_avg["Groundwater Depletion Rate (%)"],
    country_avg["Total Water Consumption (Billion m3)"],
    c=country_avg["Cluster"]
)

ax2.set_xlabel("Groundwater Depletion (%)")
ax2.set_ylabel("Water Consumption (Billion m3)")

st.pyplot(fig2)

st.subheader("📊 Feature Importance (Conceptual)")

importance = {
    "Groundwater Depletion": 0.53,
    "Rainfall Impact": 0.12,
    "Agriculture Use": 0.11,
    "Industrial Use": 0.10,
    "Consumption": 0.08,
    "Per Capita": 0.05
}

st.bar_chart(pd.Series(importance))

st.subheader("🌾 Sectoral Water Usage")

sector = df[[
    "Agricultural Water Use (%)",
    "Industrial Water Use (%)",
    "Household Water Use (%)"
]].mean()

st.bar_chart(sector)

st.subheader("📈 Future Consumption Forecast")

trend = df.groupby("Year")["Total Water Consumption (Billion m3)"].mean()

future_years = list(range(2026, 2031))
last_value = trend.iloc[-1]

forecast = [last_value * (1 + 0.02*i) for i in range(1, 6)]

forecast_df = pd.DataFrame({
    "Year": future_years,
    "Forecast": forecast
}).set_index("Year")

st.line_chart(forecast_df)


# =====================
# COUNTRY DATA
# =====================
st.subheader("🌍 Country Data")

country = st.selectbox("Select Country", df["Country"].unique())
st.write(df[df["Country"] == country])

# =====================
# YEAR ANALYSIS
# =====================
st.subheader("📅 Year-wise Analysis")

year = st.slider("Select Year", 2000, 2025)
filtered = df[df["Year"] == year]

st.bar_chart(filtered.set_index("Country")["Total Water Consumption (Billion m3)"])

# =====================
# PREDICTION
# =====================
st.subheader("🤖 Predict Water Scarcity")

consumption = st.slider("Water Consumption", 10.0, 800.0)
groundwater = st.slider("Groundwater Depletion", 0.1, 7.0)
rainfall = st.slider("Rainfall", 50.0, 3000.0)

if st.button("Predict"):

    result = predict(consumption, groundwater, rainfall)

    # Show risk score also (nice upgrade)
    risk_score = (
        0.4 * groundwater +
        0.3 * (1000 - rainfall) / 1000 +
        0.3 * (consumption / 100)
    )

    st.write("Risk Score:", round(risk_score, 2))

    if result == 2:
        st.error("🚨 High Risk")
    elif result == 1:
        st.warning("⚠️ Moderate Risk")
    else:
        st.success("✅ Low Risk")