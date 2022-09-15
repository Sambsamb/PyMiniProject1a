# Mini Project 1
>INF601 - Advanced Programming in Python
> 
>Sam Boutros
> 
>FHSU - Fall 2022
>
>9/15/2022
> 
This mini project collects the closing price of 5 stocks for the past 10 trading days, plots that information in 5 graphs, and stores these graphs as PNG files. 

The main.py file requires the following 3 packages:

* numpy
* matplotlib
* yfinance

To install these packages use:
```python
pip install -r Requirements.txt
```
The list of stocks is defined in line 30 and can be changed as desired
```python
myStockList = ["ITOT", "BA", "UNH", "BAC", "COIN"]
```
The count of days is defined in line 31 and can be changed as desired
```python
countOfDays = 10
```
The script writes progress information to the console similar to
```python
Collecting the closing price of the following 5 stock tickers for the last 10 trading days:

[*********************100%***********************]  1 of 1 completed
    Stock ITOT last 10 days price
[88.05000305175781, 88.16999816894531, 87.2699966430664, 86.91000366210938, 88.5199966430664, 89.16999816894531, 90.62999725341797, 91.66000366210938, 87.72000122070312, 88.05999755859375]
Data is stored as <class 'list'>
Data is now converted to <class 'numpy.ndarray'>
Plotting 'Adj Close' prices of the last 10 days of stock ITOT


[*********************100%***********************]  1 of 1 completed
    Stock BA last 10 days price
[160.25, 153.66000366210938, 151.82000732421875, 152.38999938964844, 155.9499969482422, 157.7899932861328, 157.52000427246094, 158.72000122070312, 147.30999755859375, 149.25999450683594]
Data is stored as <class 'list'>
Data is now converted to <class 'numpy.ndarray'>
Plotting 'Adj Close' prices of the last 10 days of stock BA


[*********************100%***********************]  1 of 1 completed
    Stock UNH last 10 days price
[517.70556640625, 522.3609619140625, 514.73486328125, 516.0607299804688, 520.0482177734375, 525.8599853515625, 524.3400268554688, 531.25, 513.9600219726562, 509.7699890136719]
Data is stored as <class 'list'>
Data is now converted to <class 'numpy.ndarray'>
Plotting 'Adj Close' prices of the last 10 days of stock UNH


[*********************100%***********************]  1 of 1 completed
    Stock BAC last 10 days price
[33.38999938964844, 33.470001220703125, 33.43000030517578, 33.060001373291016, 33.56999969482422, 34.650001525878906, 34.939998626708984, 35.27000045776367, 34.0, 33.869998931884766]
Data is stored as <class 'list'>
Data is now converted to <class 'numpy.ndarray'>
Plotting 'Adj Close' prices of the last 10 days of stock BAC


[*********************100%***********************]  1 of 1 completed
    Stock COIN last 10 days price
[66.80000305175781, 65.52999877929688, 65.26000213623047, 62.779998779296875, 68.25, 73.08000183105469, 80.87000274658203, 82.55000305175781, 75.25, 78.69999694824219]
Data is stored as <class 'list'>
Data is now converted to <class 'numpy.ndarray'>
Plotting 'Adj Close' prices of the last 10 days of stock COIN
```

The script saves the PNG images to /charts folder. It creates the folder if it did not exist. 