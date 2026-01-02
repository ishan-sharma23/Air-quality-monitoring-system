import pandas as pd
from sklearn.preprocessing import MinMaxScaler

# Load dataset
df = pd.read_csv(r"C:\Users\shakh\Desktop\air quality\archive\delhi_aqi.csv")

# Convert date column
df['date'] = pd.to_datetime(df['date'])

# Extract time features
df['hour'] = df['date'].dt.hour
df['day'] = df['date'].dt.day
df['month'] = df['date'].dt.month

# Add season column
def get_season(m):
    if m in [12, 1, 2]: return 0  # Winter
    if m in [3, 4, 5]: return 1   # Summer
    if m in [6, 7, 8, 9]: return 2 # Monsoon
    return 3  # Post-monsoon

df['season'] = df['month'].apply(get_season)

# Drop original date (not needed for ML model)
df = df.drop(columns=['date'])

# Normalize pollutant columns
pollutants = ['co','no','no2','o3','so2','pm2_5','pm10','nh3']
scaler = MinMaxScaler()
df[pollutants] = scaler.fit_transform(df[pollutants])

# Save processed data
df.to_csv(r"C:\Users\shakh\Desktop\air quality\archive\processed_aqi.csv", index=False)

print("Preprocessing complete! Saved as processed_aqi.csv")
