import numpy as np
import pandas as pd
import yfinance as yf

stocks = 'CVNA KMX AN'
stocks = stocks.split()
data = yf.download(stocks, '2017-04-28')['Close']
data.head()
