import streamlit as st
import xgboost as xgb
import pandas as pd
import plotly.express as px
import folium
from streamlit_folium import folium_static

# Load prediction model
model = xgb.XGBRegressor()
model.load_model(r"C:\Users\shakh\Desktop\air quality\archive\retrained_xgb_pm25.json")

# Load merged data for prediction
df = pd.read_csv(r"C:\Users\shakh\Desktop\air quality\archive\merged_aqi.csv")
feature_order = list(df.drop(columns=['pm2_5']).columns)

# Load original data for charts (contains 'date')
df_viz = pd.read_csv(r"C:\Users\shakh\Desktop\air quality\archive\delhi_aqi.csv")
df_viz['date'] = pd.to_datetime(df_viz['date'], errors='coerce')

# ---- UI ----
st.set_page_config(page_title="Delhi Air Quality ML", layout="wide")
st.title("Delhi Air Quality Prediction 🌍")

# ---- Charts Section ----
st.subheader("PM2.5 Trend Over Time")
fig1 = px.line(df_viz, x='date', y='pm2_5')
st.plotly_chart(fig1, use_container_width=True)

st.subheader("Seasonal Average PM2.5")
season_avg = df.groupby('season')[['pm2_5']].mean().reset_index()
fig2 = px.bar(season_avg, x='season', y='pm2_5')
st.plotly_chart(fig2, use_container_width=True)

# ---- Map Section ----
st.subheader("Delhi Region Scope")
m = folium.Map(location=[28.6, 77.1], zoom_start=9)
folium.Rectangle(bounds=[[28.4, 76.8], [28.9, 77.4]], fill=True).add_to(m)
folium_static(m)

# ---- Prediction Panel ----
st.subheader("Predict PM2.5")

co = st.slider("CO", 0.0, 1.0, 0.12)
no = st.slider("NO", 0.0, 1.0, 0.05)
no2 = st.slider("NO₂", 0.0, 1.0, 0.10)
o3 = st.slider("O₃", 0.0, 1.0, 0.20)
so2 = st.slider("SO₂", 0.0, 1.0, 0.03)
pm10 = st.slider("PM10", 0.0, 1.0, 0.25)
nh3 = st.slider("NH₃", 0.0, 1.0, 0.08)
hour = st.number_input("Hour", 0, 23, 14)
day = st.number_input("Day", 1, 31, 15)
month = st.number_input("Month", 1, 12, 11)
season = st.selectbox("Season", [0,1,2,3], format_func=lambda x: ["Winter","Summer","Monsoon","Post-Monsoon"][x])
aer_ai = st.slider("Aerosol Index", 0.0, 5.0, 1.2)

input_data = {
    "co": co,
    "no": no,
    "no2": no2,
    "o3": o3,
    "so2": so2,
    "pm10": pm10,
    "nh3": nh3,
    "hour": hour/23,
    "day": day/31,
    "month": month/12,
    "season": season,
    "aer_ai": aer_ai
}

input_df = pd.DataFrame([input_data])
input_df = input_df.reindex(columns=feature_order, fill_value=0)

if st.button("Predict PM2.5"):
    pred = model.predict(input_df)[0]
    st.success(f"Normalized PM2.5: {round(pred, 6)}")
    impact = "Severe" if pred > 0.7 else "High" if pred > 0.4 else "Moderate" if pred > 0.2 else "Low"
    st.info(f"AQI Impact Level: {impact}")

st.caption("Built by Ishan Sharma")
