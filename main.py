"""
INF601 - Advanced Programming in Python
Sam Boutros
Mini Project 1
9/15/2022
"""

# Importing the used packages
import numpy as np
import matplotlib as plt
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

ms2 = data['Adj Close']
print("Alternatively, ms2 data type is",type(ms2))

# Create a NumPy array
msftarray = np.array(msftPrices)
print("msftarray data type is",type(msftarray))

ms2array = np.array(ms2)
print("Alternatively, ms2array data type is",type(ms2array))

# Creatematplotlib graph
plt.plot(msftarray)

# Save to file
plt.savefig('charts/msft.png')

# Show the file
plt.show()