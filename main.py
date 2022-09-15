"""
(5) Initial comments with your name, class and project at the top of your .py file:

INF601 - Advanced Programming in Python
Sam Boutros
Mini Project 1
9/15/2022
"""


# (5) Proper import of packages used:
import numpy as np
import matplotlib as plt
import yfinance as yf
import datetime as dt


# (20) Collect the closing price of 5 of your favorite stock tickers for the last 10 trading days
myStockList = ["ITOT","BA","UNH","BAC","COIN"]
countOfDays = 10
enddate = dt.date.today()
startdate = enddate + dt.timedelta(days=-30)

print() # Blank line
print("Collecting the closing price of the following",len(myStockList),"stock tickers for the last",countOfDays,"trading days:")
for stock in myStockList:
    print("    ",stock)
rawData = [] # Create empty list (native 1d Py array), each list element will be raw data of one stock
for stock in myStockList:
    datum = yf.download(stock, start=startdate, end=enddate)
    rawData.append(datum[-countOfDays:]) # Add only the last "countOfDays" to our rawData list
print("done")


# (10) Store this information in a list that you will convert to a ndarray in NumPy
print()


# Get MSFt data
data = yf.download("MSFT", start="2022-08-01", end="2022-09-30")

print("Got",len(data),"days worth of MSFT stock price data.")
print(data[-10:])
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