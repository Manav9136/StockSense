import yfinance as yf
import pandas as pd

# stock symbol
ticker = "RELIANCE.NS"

# fetch 1 year of historical data
data = yf.Ticker(ticker).history(
    period='1y',
    interval='1d'
)

print("========== FIRST 5 ROWS ==========")
print(data.head())

print("\n========== LAST 5 ROWS ==========")
print(data.tail())

print("\n========== COLUMNS ==========")
print(data.columns)

print("\n========== DATA SHAPE ==========")
print(data.shape)

print("\n========== DATA TYPES ==========")
print(data.dtypes)

print("\n========== MISSING VALUES ==========")
print(data.isnull().sum())

# Save data
data.to_csv("data/reliance.csv")

print("\n Data saved successfully!")