import pandas as pd

# Load processed ground data (hourly)
df_ground = pd.read_csv(r"C:\Users\shakh\Desktop\air quality\archive\processed_aqi.csv")

# Load satellite averages
df_sat = pd.read_csv(r"C:\Users\shakh\Desktop\air quality\archive\satellite_delhi.csv")

# Convert satellite pollutants into columns instead of rows
sat_features = df_sat.set_index('pollutant').T

# Broadcast satellite features to all rows
for col in sat_features.columns:
    df_ground[col.lower()] = sat_features[col].values[0]

# Save merged dataset
df_ground.to_csv(r"C:\Users\shakh\Desktop\air quality\archive\merged_aqi.csv", index=False)

print("\nDatasets merged successfully! Saved as merged_aqi.csv")
print(df_ground.head())
