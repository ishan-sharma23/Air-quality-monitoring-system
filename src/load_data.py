import pandas as pd

df = pd.read_csv(r"C:\Users\shakh\Desktop\air quality\archive\delhi_aqi.csv")

print(df.head())
print(df.info())
print(df.describe())
print("Missing values:\n", df.isnull().sum())
