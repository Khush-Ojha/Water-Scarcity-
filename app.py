import streamlit as st
import pandas as pd
import sys
import os

sys.path.append(os.path.abspath("src"))

from predict import predict

df = pd.read_csv("data/water.csv")

st.title("🌍 AI Water Scarcity Analysis System")

st.write("AI system for analyzing and predicting global water scarcity.")

# Trend
st.subheader("📈 Global Water Consumption Trend")
trend = df.groupby("Year")["Total Water Consumption (Billion m3)"].mean()
st.line_chart(trend)

# Risk Score
df["Risk Score"] = (
    0.4 * df["Groundwater Depletion Rate (%)"] +
    0.3 * (1000 - df["Rainfall Impact (mm)"]) / 1000 +
    0.3 * df["Total Water Consumption (Billion m3)"] / 100
)

# Top 10
st.subheader("🏆 Top 10 High Risk Countries")

country_risk = df.groupby("Country")["Risk Score"].mean().reset_index()
top10 = country_risk.sort_values("Risk Score", ascending=False).head(10)

st.table(top10)

# Country Data
st.subheader("🌍 Country Data")
country = st.selectbox("Select Country", df["Country"].unique())
st.write(df[df["Country"] == country])

# Year Analysis
st.subheader("📅 Year-wise Analysis")
year = st.slider("Select Year", 2000, 2025)
filtered = df[df["Year"] == year]

st.bar_chart(filtered.set_index("Country")["Total Water Consumption (Billion m3)"])

# Prediction
st.subheader("🤖 Predict Water Scarcity")

consumption = st.slider("Water Consumption", 10.0, 800.0)
groundwater = st.slider("Groundwater Depletion", 0.1, 7.0)
rainfall = st.slider("Rainfall", 50.0, 3000.0)

if st.button("Predict"):
    result = predict(consumption, groundwater, rainfall)

    if result == 2:
        st.error("🚨 High Risk")
    elif result == 1:
        st.warning("⚠️ Moderate Risk")
    else:
        st.success("✅ Low Risk")