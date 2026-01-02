# Air Quality Monitoring and Prediction Using Sentinel-5P (TROPOMI) and Machine Learning

## 🌍 Project Overview
This project builds an **end-to-end air quality analytics system** using satellite data from **Sentinel-5P TROPOMI** and machine learning regression models to predict **daily mean PM2.5 concentration**. It includes pollutant trend visualization, data preprocessing, model training, and an interactive dashboard for real-time predictions.

## 📊 Key Features
- **Satellite-based pollutant extraction** (Aerosol Index used as PM2.5 proxy)
- **Daily mean aggregation** of pollutant signals
- **Dataset merging** with ground-truth PM2.5 values
- **Regression model training** (Linear, Random Forest, XGBoost)
- **Performance evaluation** using MAE, RMSE, and R²
- **Streamlit dashboard** for monitoring and prediction
- **Feature importance analysis & visualization**

## 🧠 Target Variable
- **Daily Mean PM2.5 (µg/m³)** — measures fine particulate pollution in the air.
- Predicted values are mapped into AQI categories:  
  `Good → Satisfactory → Moderate → Poor → Very Poor → Severe`

## 📁 Repository Structure

