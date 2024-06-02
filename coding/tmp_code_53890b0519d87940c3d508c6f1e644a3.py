# python code
import yfinance as yf
import matplotlib.pyplot as plt
import datetime

#Today's date
today = datetime.datetime.strptime('2024-05-30', '%Y-%m-%d')

# Getting Year to Date (YTD) data:
# Start date would be the start of this year
start_date = datetime.datetime(today.year, 1, 1)
nvda = yf.download('NVDA', start=start_date.strftime('%Y-%m-%d'), end=today.strftime('%Y-%m-%d'))
tsla = yf.download('TSLA', start=start_date.strftime('%Y-%m-%d'), end=today.strftime('%Y-%m-%d'))

# Calculating gain which is percentage change from first value
nvda_gain = (nvda['Close'] / nvda['Close'].iloc[0] - 1) * 100
tsla_gain = (tsla['Close'] / tsla['Close'].iloc[0] - 1) * 100

# Plotting gain for NVDA and TSLA
plt.plot(nvda_gain, label='NVDA')
plt.plot(tsla_gain, label='TSLA')

# Setting title and labels for the plot
plt.title('Stock Gain YTD for NVDA and TSLA')
plt.xlabel('Date')
plt.ylabel('Gain (%)')

# Adding legend to the plot
plt.legend()

# Saving figure as ytd_stock_gains.png
plt.savefig('ytd_stock_gains.png')