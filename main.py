"""
(5) Initial comments with your name, class and project at the top of your .py file:
INF601 - Advanced Programming in Python
Sam Boutros
Mini Project 1
9/15/2022
"""


# (5) Proper import of packages used:
import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf
import datetime as dt
import os


def get_stock_info(fstock, fcountofdays):
    enddate = dt.date.today()
    startdate = enddate + dt.timedelta(days=-(fcountofdays + 20))
    datum = yf.download(fstock, start=startdate, end=enddate)
    lastxdays = datum[-fcountofdays:]
    fpricedata = []  # Declare a Py list
    for price in lastxdays['Adj Close']:
        fpricedata.append(price)
    return fpricedata


# (20) Collect the closing price of 5 of your favorite stock tickers for the last 10 trading days
myStockList = ["ITOT", "BA", "UNH", "BAC", "COIN"]
countOfDays = 10
if not os.path.exists('charts'):
    os.makedirs('charts')
print()  # Blank line
print("Collecting the closing price of the following", len(myStockList), "stock tickers for the last", countOfDays,
      "trading days:")
print()
for stock in myStockList:
    pricedata = get_stock_info(stock, countOfDays)
    print("    Stock", stock, "last", countOfDays, "days price")
    print(pricedata)
# (10) Store this information in a list that you will convert to a ndarray in NumPy
    print("Data is stored as", type(pricedata))  # Data is stored in <class 'list'>
    myNumPyArray = np.array(pricedata)
    print("Data is now converted to", type(myNumPyArray))  # Data is now converted to <class 'numpy.ndarray'>
    print("Plotting 'Adj Close' prices of the last", countOfDays, "days of stock", stock)
# (10) Plot the graph
    plt.plot(myNumPyArray)
# Plot improvements
    title = "Adjusted closing price of " + stock + " stock in the past " + str(countOfDays) + " days"
    plt.title(title, fontsize=13)
    plt.xlabel('Day')
    plt.ylabel('Price ($)')
    plt.grid()
# (10) Save the graph in a folder called charts as PNG file
    plt.savefig('charts/' + stock + '.png')
    plt.show()
    print()
    print()
