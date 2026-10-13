# 📈 StockSense — Indian Stock Market Analyzer

StockSense is a Python-based stock market analysis dashboard that helps users explore Indian stock prices, returns, volatility, and historical performance through interactive visualizations.

## ✨ Features

- **Stock Selection:** Analyze Reliance Industries, TCS, Infosys, HDFC Bank, ICICI Bank, and SBI.
- **Historical Price Analysis:** Explore stock prices across different time periods.
- **Moving Averages:** View 20-day and 50-day moving averages.
- **Trading Volume:** Visualize historical trading activity.
- **Daily Returns:** Understand daily percentage price changes.
- **Historical Drawdown:** Examine declines from previous price peaks.
- **Stock Comparison:** Compare the percentage performance of two stocks.
- **Data Lab:** Calculate average daily return, annualized volatility, and maximum drawdown.
- **Interactive Dashboard:** Explore charts and metrics using Streamlit and Plotly.

## 🛠️ Technologies Used

- Python
- Streamlit
- Pandas
- NumPy
- yfinance
- Plotly

## 📂 Project Structure

```text
StockSense/
├── app.py
├── analysis.py
├── data_fetcher.py
├── visualization.py
├── requirements.txt
├── README.md
├── assets/
│   └── stocksense_logo.png
└── data/
```

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd StockSense
```

### 2. Create a virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Run the dashboard

```bash
python -m streamlit run app.py
```

The dashboard will open in your browser.

## 📊 Data Source

Historical stock data is retrieved using the `yfinance` Python library. Data availability and accuracy depend on the upstream provider.

## 🎯 Project Objective

The objective of StockSense is to practice Python programming, financial data analysis, data visualization, and interactive dashboard development.

## ⚠️ Disclaimer

StockSense is an educational project, not financial advice. Historical performance does not guarantee future returns.

## 👨‍💻 Author

Developed as a Python and data analytics portfolio project.