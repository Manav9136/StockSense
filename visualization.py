import plotly.express as px
import pandas as pd

data = pd.read_csv("data/reliance_analyzed.csv")

data["Date"] = pd.to_datetime(data["Date"])

# create closing price chart

fig = px.line(
    data,
    x="Date",
    y="Close",
    title="Reliance Industries - Closing Price"
)

# chart label update
fig.update_layout(
    xaxis_title = "Date",
    yaxis_title = "Closing Price (rupee)"
)

# show chart
fig.show()