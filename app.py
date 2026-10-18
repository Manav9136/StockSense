import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import yfinance as yf

st.set_page_config(
    page_title="StockSense",
    page_icon="📈",
    layout="wide"
)

st.sidebar.image(
    "assets/logo.png",
    width=160
)

st.sidebar.write("Indian Stock Market Analyzer")
st.sidebar.caption("Your Indian Stock Market Dashboard")

logo_col, title_col = st.columns([1, 5])

with logo_col:
    st.image("assets/logo.png", width=100)

with title_col:
    st.title("StockSense")
    st.caption(
        "Analyze stock prices, returns, volatility, and market performance."
    )

stock = st.selectbox(
    "Select a stock",
    ["RELIANCE.NS", "TCS.NS", "INFY.NS",
     "HDFCBANK.NS", "ICICIBANK.NS", "SBIN.NS"]
)

st.subheader(f"{stock} - Stock Analysis")

ticker = yf.Ticker(stock)


period_options = {
    "1 Month": "1mo",
    "3 Months": "3mo",
    "6 Months": "6mo",
    "1 Year": "1y",
    "5 Years": "5y"
}

selected_period = st.selectbox(
    "Select time period",
    list(period_options.keys()),
    index=3
)

period = period_options[selected_period]

data = ticker.history(
    period=period,
    interval="1d"
)


data["Daily Return"] = data["Close"].pct_change()
data["Daily Return (%)"] = data["Daily Return"] * 100
data["MA20"] = data["Close"].rolling(window=20).mean()
data["MA50"] = data["Close"].rolling(window=50).mean()
data["Running Max"] = data["Close"].cummax()

data["Drawdown (%)"] = (
    (data["Close"] - data["Running Max"])
    / data["Running Max"]
) * 100

data = data.reset_index()

latest_price = data["Close"].iloc[-1]
highest_price = data["Close"].max()
lowest_price = data["Close"].min()

st.header("🧪 Data Lab")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "💰 Latest Price",
        f"₹{latest_price:,.2f}"
    )

with col2:
    st.metric(
        "📈 Highest Price",
        f"₹{highest_price:,.2f}"
    )

with col3:
    st.metric(
        "📉 Lowest Price",
        f"₹{lowest_price:,.2f}"
    )

# ==================================================
# PRICE CHART
# ==================================================

fig_price = go.Figure()

# Closing price
fig_price.add_trace(
    go.Scatter(
        x=data["Date"],
        y=data["Close"],
        mode="lines",
        name="Closing Price"
    )
)

# 20-day moving average
fig_price.add_trace(
    go.Scatter(
        x=data["Date"],
        y=data["MA20"],
        mode="lines",
        name="MA20"
    )
)

# 50-day moving average
fig_price.add_trace(
    go.Scatter(
        x=data["Date"],
        y=data["MA50"],
        mode="lines",
        name="MA50"
    )
)

st.subheader("📈 Price Trend")

fig_price.update_layout(
    title=f"{stock} - Price Trend",
    xaxis_title="Date",
    yaxis_title="Price (₹)",
    hovermode="x unified"
)

st.plotly_chart(
    fig_price,
    width="stretch"
)


# ==================================================
# VOLUME CHART
# ==================================================


fig_volume = go.Figure()

fig_volume.add_trace(
    go.Bar(
        x=data["Date"],
        y=data["Volume"],
        name="Trading Volume"
    )
)

st.subheader("📊 Trading Volume")

fig_volume.update_layout(
    title="Reliance Industries - Trading Volume",
    xaxis_title="Date",
    yaxis_title="Volume",
    hovermode="x unified"
)

st.plotly_chart(
    fig_volume,
    width="stretch"
)


# ==================================================
# DAILY RETURN CHART
# ==================================================


fig_return = go.Figure()

fig_return.add_trace(
    go.Scatter(
        x=data["Date"],
        y=data["Daily Return (%)"],
        mode="lines",
        name="Daily Return"
    )
)

st.subheader("📉 Daily Returns")

fig_return.update_layout(
    title="Reliance Industries - Daily Return",
    xaxis_title="Date",
    yaxis_title="Daily Return (%)",
    hovermode="x unified"
)

st.plotly_chart(
    fig_return,
    width="stretch"
)


# ==================================================
# DRAWDOWN CHART
# ==================================================


fig_drawdown = go.Figure()

fig_drawdown.add_trace(
    go.Scatter(
        x=data["Date"],
        y=data["Drawdown (%)"],
        mode="lines",
        name="Drawdown"
    )
)

st.subheader("⚠️ Historical Drawdown")

fig_drawdown.update_layout(
    title="Reliance Industries - Historical Drawdown",
    xaxis_title="Date",
    yaxis_title="Drawdown (%)",
    hovermode="x unified"
)

st.plotly_chart(
    fig_drawdown,
    width="stretch"
)

st.header("Stock Comparison")

compare1, compare2 = st.columns(2)

with compare1:
    stock1 = st.selectbox(
        "First stock",
        ["RELIANCE.NS", "TCS.NS", "INFY.NS"],
        key="compare_stock1"
    )

comparison_options = [
    symbol
    for symbol in ["RELIANCE.NS", "TCS.NS", "INFY.NS"]
    if symbol != stock1
]

with compare2:
    stock2 = st.selectbox(
        "Second stock",
        comparison_options,
        key="compare_stock2"
    )

data1 = yf.Ticker(stock1).history(period="1y")
data2 = yf.Ticker(stock2).history(period="1y")

if data1.empty or data2.empty:
    st.error("Unable to fetch data for one or both stocks.")
    st.stop()

data1["Return (%)"] = (
    data1["Close"] / data1["Close"].iloc[0] - 1
) * 100

data2["Return (%)"] = (
    data2["Close"] / data2["Close"].iloc[0] - 1
) * 100

fig_compare = go.Figure()

fig_compare.add_trace(
    go.Scatter(
        x=data1.index,
        y=data1["Return (%)"],
        mode="lines",
        name=stock1
    )
)

fig_compare.add_trace(
    go.Scatter(
        x=data2.index,
        y=data2["Return (%)"],
        mode="lines",
        name=stock2
    )
)

st.subheader("🔍 Stock Performance Comparison")

fig_compare.update_layout(
    xaxis_title="Date",
    yaxis_title="Return (%)",
    hovermode="x unified"
)

st.plotly_chart(fig_compare, width="stretch")

final_return1 = data1["Return (%)"].iloc[-1]
final_return2 = data2["Return (%)"].iloc[-1]

compare_col1, compare_col2 = st.columns(2)

with compare_col1:
    st.metric(
        f"{stock1} Total Return",
        f"{final_return1:.2f}%"
    )

with compare_col2:
    st.metric(
        f"{stock2} Total Return",
        f"{final_return2:.2f}%"
    )

if final_return1 > final_return2:
    st.success(f"{stock1} performed better over this period.")
elif final_return2 > final_return1:
    st.success(f"{stock2} performed better over this period.")
else:
    st.info("Both stocks had the same return.")


st.header("Data Lab")

average_daily_return = data["Daily Return (%)"].mean()
st.metric(
    "Average Daily Return",
    f"{average_daily_return:.2f}%"
)

daily_volatility = data["Daily Return (%)"].dropna().std()

annualized_volatility = daily_volatility * (252 ** 0.5)

max_drawdown = data["Drawdown (%)"].min()

st.metric(
    "Annualized Volatility",
    f"{annualized_volatility:.2f}%"
)

st.metric(
    "Maximum Drawdown",
    f"{max_drawdown:.2f}%"
)
