import pandas as pd
import matplotlib.pyplot as plt

# Load original data for EDA
df = pd.read_csv(r"C:\Users\shakh\Desktop\air quality\archive\delhi_aqi.csv")
df['date'] = pd.to_datetime(df['date'])

# 1. Pollutant trend (PM2.5 over time)
plt.figure()
plt.plot(df['date'], df['pm2_5'])
plt.title("PM2.5 Trend Over Time")
plt.xlabel("Date")
plt.ylabel("PM2.5")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 2. Seasonal average pollution
df['month'] = df['date'].dt.month
df['season'] = df['month'].apply(lambda m: 0 if m in [12,1,2] else 1 if m in [3,4,5] else 2 if m in [6,7,8,9] else 3)

seasonal = df.groupby('season')[['pm2_5','pm10','co','no2','so2','o3','nh3']].mean()

plt.figure()
plt.bar(seasonal.index, seasonal['pm2_5'])
plt.title("Average PM2.5 by Season")
plt.xlabel("Season (0:Winter,1:Summer,2:Monsoon,3:Post-Monsoon)")
plt.ylabel("Avg Normalized PM2.5")
plt.tight_layout()
plt.show()

# 3. Histogram of AQI values
plt.figure()
plt.hist(df['pm2_5'], bins=30)
plt.title("Distribution of PM2.5")
plt.xlabel("PM2.5")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()

print("\nSeasonal Pollution Table:\n", seasonal)
