import numpy as np
import pandas as pd
import yfinance as yf

stocks = 'CVNA KMX AN'
stocks = stocks.split()
data = yf.download(stocks, '2017-04-28')['Close']
data.head(600)

#fedData = pd.read_csv("usedCars.csv")
#fedData.set_index('Date', inplace=True)
#fedData.head(30)
#I was trying to put used car sales data on a seperate y axis to see if there was any correlation but had no luck in figuring out how to do so in python
#I assume using montly historical price data might change my results

import matplotlib.pyplot as plt
%matplotlib inline
plt.figure(figsize=(17,10))
plt.plot(data)
plt.legend(['AN', 'CVNA', 'KMX'], loc=2)

returns = pd.DataFrame()
for stock in data:
    if stock not in returns:
        returns[stock] = np.log(data[stock]).diff()
returns = returns[1:]
returns.head(600)

returns.describe()

returns.corr()

from pandas.plotting import scatter_matrix
scatter_matrix(returns, figsize=(17,10), alpha=0.4)
