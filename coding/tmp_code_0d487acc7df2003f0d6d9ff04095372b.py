# Import necessary functions
from functions import get_stock_prices, plot_stock_prices
# Provide the stock symbols
stock_symbols = ['NVDA', 'TSLA']
# Determine the start and end dates
start_date = '2024-01-01'
end_date = '2024-05-30'
# Retrieve the stock prices
stock_prices = get_stock_prices(stock_symbols, start_date, end_date)
# Plot the stock prices
filename = 'stock_prices_YTD_plot.png'
plot_stock_prices(stock_prices, filename)
print("The plot is successfully saved to file '{}'".format(filename))