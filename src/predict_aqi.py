import xgboost as xgb
import pandas as pd
import numpy as np

# Load retrained model
model = xgb.XGBRegressor()
model.load_model(r"C:\Users\shakh\Desktop\air quality\archive\retrained_xgb_pm25.json")

# Load merged dataset to get feature structure
df = pd.read_csv(r"C:\Users\shakh\Desktop\air quality\archive\merged_aqi.csv")
X_sample = df.drop(columns=['pm2_5']).head(1)

# ---- New input sample (modify values as needed) ----
new_data = {
    "co": 0.12,
    "no": 0.05,
    "no2": 0.10,
    "o3": 0.20,
    "so2": 0.03,
    "pm10": 0.25,
    "nh3": 0.08,
    "hour": 14/23,
    "day": 15/31,
    "month": 12/12,
    "no2": df['no2'].mean(),
    "so2": df['so2'].mean(),
    "co": df['co'].mean(),
    "o3": df['o3'].mean(),
    "aer_ai": df['aer_ai'].mean()
}

# Convert to DataFrame with same columns as training
input_df = pd.DataFrame([new_data])
input_df = input_df.reindex(columns=X_sample.columns, fill_value=0)

# Predict
prediction = model.predict(input_df)

print("\nPredicted Normalized PM2.5:", round(prediction[0], 6))
print("Estimated AQI Impact Level:",
      "Severe" if prediction[0] > 0.7 else
      "High" if prediction[0] > 0.4 else
      "Moderate" if prediction[0] > 0.2 else
      "Low")
