import streamlit as st
import pandas as pd

df = pd.read_csv("data/water.csv")

st.title("AI-Based Water Scarcity System")

# =====================
# TREND
# =====================
st.subheader("Water Consumption Trend")
trend = df.groupby("Year")["Total Water Consumption (Billion m3)"].mean()
st.line_chart(trend)

# =====================
# SECTOR
# =====================
st.subheader("Sector Usage")
sector = df[[
"Agricultural Water Use (%)",
"Industrial Water Use (%)",
"Household Water Use (%)"
]].mean()

st.bar_chart(sector)

# =====================
# COUNTRY FILTER
# =====================
st.subheader("Country Data")
country = st.selectbox("Select Country", df["Country"].unique())
st.write(df[df["Country"] == country])

# =====================
# ADVANCED: PREDICTION TOOL
# =====================
st.subheader("Predict Water Risk")

consumption = st.slider("Water Consumption", 10.0, 800.0)
groundwater = st.slider("Groundwater Depletion", 0.1, 7.0)
rainfall = st.slider("Rainfall", 50.0, 3000.0)

if st.button("Predict"):
    score = 0.4*groundwater + 0.3*(1000-rainfall)/1000 + 0.3*(consumption/100)

    if score > 3:
        st.error("High Risk")
    elif score > 2:
        st.warning("Moderate Risk")
    else:
        st.success("Low Risk")