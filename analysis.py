import pandas as pd
import numpy as np

# load stock data
data = pd.read_csv("data/reliance.csv")

# convert date column to datetime
data["Date"] = pd.to_datetime(data["Date"])

# sort by date
data = data.sort_values("Date")

# daily return
data["Daily Return"] = data["Close"].pct_change()

# daily return in %
data["Daily Return (%)"] = data["Daily Return"] * 100

# 20-day moving average
data["MA20"] = data["Close"].rolling(window=20).mean()

# 50-day moving average
data["MA50"] = data["Close"].rolling(window=50).mean()


# ==================================================
# VOLATILITY
# ==================================================

volatility = np.std(
    data["Daily Return (%)"].dropna()
)

print("\n========== VOLATILITY ==========")
print(f"Daily volatility: {volatility:.2f}%")

annualized_volatility = volatility * np.sqrt(252)

print(
    f"Annualized volatility: "
    f"{annualized_volatility:.2f}%"
)


# ==================================================
# RUNNING MAX & DRAWDOWN
# ==================================================

data["Running Max"] = data["Close"].cummax()

data["Drawdown (%)"] = (
    (data["Close"] - data["Running Max"])
    / data["Running Max"]
) * 100

max_drawdown = data["Drawdown (%)"].min()


# ==================================================
# STOCK ANALYSIS
# ==================================================

print("\n========== STOCK ANALYSIS ==========")

print(
    data[
        [
            "Date",
            "Close",
            "Daily Return (%)",
            "MA20",
            "MA50",
            "Running Max",
            "Drawdown (%)"
        ]
    ].tail(10)
)


# ==================================================
# STOCK SUMMARY
# ==================================================

latest_close = data["Close"].iloc[-1]
highest_price = data["Close"].max()
lowest_price = data["Close"].min()
average_price = data["Close"].mean()
total_trading_days = len(data)

print("\n========== STOCK SUMMARY ==========")

print(f"Latest closing price: ₹{latest_close:.2f}")
print(f"Highest closing price: ₹{highest_price:.2f}")
print(f"Lowest closing price: ₹{lowest_price:.2f}")
print(f"Average closing price: ₹{average_price:.2f}")
print(f"Total trading days: {total_trading_days}")
print(f"Daily volatility: {volatility:.2f}%")
print(f"Annualized volatility: {annualized_volatility:.2f}%")
print(f"Maximum drawdown: {max_drawdown:.2f}%")


# ==================================================
# SAVE ANALYZED DATA
# ==================================================

data.to_csv(
    "data/reliance_analyzed.csv",
    index=False
)

print("\nAnalyzed data saved successfully!")