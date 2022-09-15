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


# (20) Collect the closing price of 5 of your favorite stock tickers for the last 10 trading days
myStockList = ["ITOT", "BA", "UNH", "BAC", "COIN"]
countOfDays = 10
enddate = dt.date.today()
startdate = enddate + dt.timedelta(days=-30)
print()  # Blank line
print("Collecting the closing price of the following", len(myStockList), "stock tickers for the last", countOfDays, "trading days:")
myVars = locals()
for stock in myStockList:
    datum = yf.download(stock, start=startdate, end=enddate)
    lastDays = datum[-countOfDays:]
    myVars[stock] = []  # Declare a 'local' variable with the name of the current stock as a Py list
    for price in lastDays['Adj Close']:
        myVars[stock].append(price)
    print()
    print("    Stock", stock, "last", countOfDays, "days price")
    print(myVars[stock])
print()
print("Data is stored as", type(myVars[stock]))  # Data is stored in <class 'list'>


# (10) Store this information in a list that you will convert to a ndarray in NumPy
myNumPyArray = np.array([ITOT, BA, UNH, BAC, COIN])
print()
print("Loaded up the raw data into a NumPy array", '"myNumPyArray"', type(myNumPyArray))
print("This is a 2 dimensional array, with the following shape/dimensions:", myNumPyArray.shape)
print("The first dimension is the Price, for example the price of all ten days of the fifth stock 'COIN' can be referenced as 'myNumPyArray[4]'")
print(myNumPyArray[4])  # Prices of the last stock 'COIN' (all 10 days)
print("The second dimension is the Price of a specific Date, for example the Price of the tenth day of the fifth stock 'COIN' can be referenced as 'myNumPyArray[4,9]'")
print(myNumPyArray[4, 9])  # Price of the tenth day of the fifth stock 'COIN'


# (10) Plot these 5 graphs
# (10) Save these graphs in a folder called charts as PNG files
if not os.path.exists('charts'):
    os.makedirs('charts')
print()
i = 0
for stock in myStockList:
    print("Plotting 'Adj Close' values of the last", countOfDays, "days of stock", stock)
    plt.plot(myNumPyArray[i])
    plt.savefig('charts/' + stock + '.png')
    plt.show()
    i += 1

