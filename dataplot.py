import pandas as pd
import plotly.express as px


columns = ["Date", "Supply"]
df = pd.read_csv("HistoricalData.csv", usecols=columns)
print("Contents in csv file:\n", df)

fig = px.line(df, x = 'Date', y = 'Supply', title='Uniswap Supply')
fig.show()