import streamlit as st
import pandas as pd
import sys
import os


# =====================
# FIX IMPORT PATH
# =====================
sys.path.append(os.path.abspath("src"))

from predict import predict

# =====================
# LOAD DATA
# =====================
df = pd.read_csv("data/water.csv")

# =====================
# TITLE
# =====================
st.title("🌍 AI-Based Water Scarcity Analysis System")
st.write("This AI system analyzes global water consumption trends and predicts water scarcity risk using machine learning models.")

# =====================
# TREND GRAPH
# =====================
st.subheader("📈 Global Water Consumption Trend")

trend = df.groupby("Year")["Total Water Consumption (Billion m3)"].mean()
st.line_chart(trend)


# =====================
# TOP 10 COUNTRIES
# =====================
st.subheader("🏆 Top 10 High Risk Countries (2025)")

latest = df[df["Year"] == 2025]

top10 = latest.sort_values("Risk Score", ascending=False).head(10)

st.table(top10[["Country", "Risk Score"]])

# =====================
# COUNTRY FILTER
# =====================
st.subheader("🌍 Country Data")

country = st.selectbox("Select Country", df["Country"].unique())

st.write(df[df["Country"] == country])

# =====================
# YEAR-WISE ANALYSIS
# =====================
st.subheader("📅 Year-wise Analysis")

year = st.slider("Select Year", 2000, 2025)

filtered = df[df["Year"] == year]

st.bar_chart(filtered.set_index("Country")["Total Water Consumption (Billion m3)"])

# =====================
# PREDICTION SECTION
# =====================
st.subheader("🤖 Predict Water Scarcity")

consumption = st.slider("Water Consumption (Billion m3)", 10.0, 800.0)
groundwater = st.slider("Groundwater Depletion Rate (%)", 0.1, 7.0)
rainfall = st.slider("Rainfall Impact (mm)", 50.0, 3000.0)

if st.button("Predict"):
    result = predict(consumption, groundwater, rainfall)

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