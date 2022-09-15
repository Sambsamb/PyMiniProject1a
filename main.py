"""
INF601 - Advanced Programming in Python
Sam Boutros
Mini Project 1
9/15/2022
"""

import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf

# Get MSFt data
data = yf.download("MSFT", start="2022-09-01", end="2022-09-30")

print("Got",len(data),"days worth of MSFT stock price data.")

# Create empty list (native 1d Py array):
msftPrices = []

# Populate list:
for price in data['Adj Close']:
    msftPrices.append(price)

print(msftPrices)

print("msftPrices data type is",type(msftPrices))

# Create a NumPy array
msftarray = np.array(msftPrices)

# Creatematplotlib graph
plt.plot(msftarray)

# Save to file
plt.savefig('charts/msft.png')

# Show the file
plt.show()