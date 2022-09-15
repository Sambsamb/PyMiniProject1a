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

# Show raw data collected:
i = 0
for stock in myStockList:
    print()
    print("Stock",stock,"raw data:")
    print(rawData[i])
    i += 1


# (10) Store this information in a list that you will convert to a ndarray in NumPy
myNumPyArray = np.array([rawData[0], rawData[1], rawData[2], rawData[3], rawData[4]])
# Technically the input rawData[0] is <class 'pandas.core.frame.DataFrame'> and not <class 'list'> but the resulting NumPy ndarray array works

print()
print("Loaded up the raw data into a NumPy array",'"myNumPyArray"',type(myNumPyArray))
print("This is a 3 dimentional array, with the following shape/dimensions:",myNumPyArray.shape)
print("The first dimension is the 'stock', for example the metrics of all ten days of the fifth stock 'COIN' can be referenced as 'myNumPyArray[4]'")
print(myNumPyArray[4]) # Data of the last stock 'COIN' (all 10 days, all 6 metrics)
print("The second dimension is the 'date', for example metrics of the tenth day the fifth stock 'COIN' can be referenced as 'myNumPyArray[4,9]':")
print(myNumPyArray[4,9]) # Metrics (Open, High, Low, Close, Adj Close, Volume) of the tenth day of the fifth stock 'COIN'
print("The third dimension is a specific metric of a specific date of a specific stock, for example the 'Adj Close' of the tenth day the fifth stock 'COIN' can be referenced as 'myNumPyArray[4,9,4]':")
print(myNumPyArray[4,9,4]) # 'Adj Close' of the tenth day of 'COIN'
print("The following expression returns the 'Adj Close' of all 10 days of the fifth stock 'COIN' 'myNumPyArray[4,:10,4]':")
print(myNumPyArray[4,:10,4]) # 'Adj Close' of all 10 days of 'COIN'



