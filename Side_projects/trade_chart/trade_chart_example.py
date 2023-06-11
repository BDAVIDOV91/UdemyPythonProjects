import pandas as pd
import matplotlib.pylab as plt
import mplfinance as mpf

# Read the historical data from the CSV file
data = pd.read_csv('historical_data.csv')

# Convert the 'Date' column to a datetime object
data['Data'] = pd.to_datetime(data['Data'])

# Set the 'Date' column as the index
data.set_index('Data', inplace = True)

# Create a candlestick chart using mplfinance
mpf.plot(data, type = 'candle',  volume = True, style = 'yahoo')

# Display the chart
plt.show