import streamlit as st
import pandas as pd
import sys
import os

sys.path.append(os.path.abspath("src"))

from predict import predict

df = pd.read_csv("data/water.csv")

st.title("AI Water Scarcity Analysis")

# Trend
st.subheader("Water Consumption Trend")
trend = df.groupby("Year")["Total Water Consumption (Billion m3)"].mean()
st.line_chart(trend)

# Country Data
st.subheader("Country Data")
country = st.selectbox("Select Country", df["Country"].unique())
st.write(df[df["Country"] == country])

# Prediction
st.subheader("Predict Water Scarcity")

consumption = st.slider("Water Consumption", 10.0, 800.0)
groundwater = st.slider("Groundwater Depletion", 0.1, 7.0)
rainfall = st.slider("Rainfall", 50.0, 3000.0)

if st.button("Predict"):
    result = predict(consumption, groundwater, rainfall)

    if result == 2:
        st.error("High Risk")
    elif result == 1:
        st.warning("Moderate Risk")
    else:
        st.success("Low Risk")