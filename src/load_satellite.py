import ee
import pandas as pd

ee.Initialize(project='air-quality-ml')

region = ee.Geometry.Rectangle([76.8, 28.4, 77.4, 28.9])

# Only bands that exist in these images
bands = {
    "NO2": ("COPERNICUS/S5P/NRTI/L3_NO2", "NO2_column_number_density"),
    "SO2": ("COPERNICUS/S5P/NRTI/L3_SO2", "SO2_column_number_density"),
    "CO":  ("COPERNICUS/S5P/NRTI/L3_CO",  "CO_column_number_density"),
    "O3":  ("COPERNICUS/S5P/NRTI/L3_O3",  "O3_column_number_density"),
    "AER_AI": ("COPERNICUS/S5P/NRTI/L3_AER_AI", "absorbing_aerosol_index")
    #  CH4 removed temporarily
}

start_date = '2020-11-01'
end_date   = '2020-11-30'

sat_rows = []

for name, (path, band) in bands.items():
    img = ee.ImageCollection(path).filterDate(start_date, end_date).mean().clip(region)
    stats = img.select(band).reduceRegion(
        reducer=ee.Reducer.mean(),
        geometry=region,
        scale=1000,
        bestEffort=True
    )
    result = stats.getInfo()
    mean_val = result.get(band, None) if result else None

    sat_rows.append({"pollutant": name, "mean_concentration": mean_val})

df_sat = pd.DataFrame(sat_rows)
df_sat.to_csv(r"C:\Users\shakh\Desktop\air quality\archive\satellite_delhi.csv", index=False)

print("\nSatellite data extracted & saved!")
print(df_sat)
