# 🌍 AI Water Scarcity Analysis System

An interactive AI-powered dashboard to analyze global water consumption trends and predict water scarcity risks across countries (2000–2025).

---

## 🚀 Live Demo

👉 [**Water Scarcity Analysis App**](https://khush-ojha-water-scarcity--app-erxedi.streamlit.app/)

---

## 📌 Project Overview

This project leverages data analytics and rule-based logic to:

- **Analyze** global water consumption trends.
- **Identify** high-risk countries based on computed metrics.
- **Visualize** country-wise and year-wise insights.
- **Predict** water scarcity risk levels based on key environmental factors.

---

## ✨ Features

### 📈 Trend Analysis
- Visualizes global water consumption over time.
- Helps understand long-term historical patterns.

### 🌍 Country-Level Insights
- Explore detailed data for each specific country.
- Includes total consumption, per capita usage, and localized factors.

### 🏆 Top 10 High-Risk Countries
- Ranks countries based on a dynamically computed risk score.
- Uses aggregated metrics for accurate cross-regional comparison.

### 📅 Year-wise Analysis
- Interactive slider to analyze data for a specific year.
- Dynamic bar charts for visual comparison between regions.

### 🤖 Risk Prediction System
- Predicts water scarcity level classification (**Low** / **Moderate** / **High**).
- Based on dynamic user-controlled inputs:
  - `Water Consumption`
  - `Groundwater Depletion`
  - `Rainfall Impact`

---

## 🧠 Risk Score Logic

A composite **Risk Score** is calculated using the following formula:

> **Risk Score** = `(0.4 × Groundwater Depletion) + [0.3 × (1000 - Rainfall Factor) / 1000] + [0.3 × (Water Consumption / 100)]`

Based on the resulting score, conditions are flagged as:

- 🚨 **High Risk**: `> 3`
- ⚠️ **Moderate Risk**: `2 – 3`
- ✅ **Low Risk**: `< 2`

---

## 🛠️ Tech Stack

- **Python** 🐍
- **Streamlit** 🌐
- **Pandas** 📊
- **NumPy** 🔢

---

## ⚙️ Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/water-scarcity-ai.git
   cd water-scarcity-ai
   ```

2. **Install dependencies:**
   ```bash
   pip install -r Requirements.txt
   ```

3. **Run the application:**
   ```bash
   streamlit run app.py
   ```
