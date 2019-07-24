import numpy as np
import pandas as pd
import yfinance as yf

stocks = 'CVNA KMX AN'
stocks = stocks.split()
data = yf.download(stocks, '2017-04-28')['Close']
data.head(600)

import matplotlib.pyplot as plt
%matplotlib inline
plt.figure(figsize=(17,10))
plt.plot(data)
plt.legend(['AN', 'CVNA', 'KMX'], loc=2)
