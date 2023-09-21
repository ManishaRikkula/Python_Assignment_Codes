#!/usr/bin/env python
# coding: utf-8

# 1. Download the close prices of Apple, Google and Meta from yahoo finance for past 10 year				
# 2. merge all three dataframes on Date column				
# 3. calculate log returns of the close price for each of the stock				
# 4. Calculate 99 percentile, 95 percentile, 90 percentile VaR number for the portfolio				
# 5. Repeat the above exercise for different holding period such as 1day, 2day, 5day and 10day respectively				
# 6. Create a summary dataframe to show the comparison of Holding Period vs Confidence level				
# 				
# 	Confidence Level	99%	95%	90%
# 	1day	VaR1	VaR4	VaR7
# 	2day	VaR2	VaR5	VaR8
# 	5day	VaR3	VaR6	VaR9
# 	10day	VaR10	VaR11	VaR12
# 

# In[ ]:


import pandas as pd
import numpy as np
import yfinance as yf
from scipy.stats import norm


# In[2]:



# list of stock symbols
stock_symbols = ['AAPL', 'GOOGL', 'META']

# start and end dates for the data
start_date = '2013-08-21'
end_date = '2023-08-21'

# Download the close prices
stock_data = yf.download(stock_symbols, start=start_date, end=end_date)['Close']

# log returns
log_returns = np.log(stock_data / stock_data.shift(1))

# holding periods
holding_periods = [1, 2, 5, 10]  # in days

#  portfolio returns as the sum of individual stock log returns
portfolio_returns = log_returns.sum(axis=1)

#  confidence levels
confidence_levels = [0.99, 0.95, 0.90]

# VaR for different holding periods and confidence levels
var_results = []

for period in holding_periods:
    var_row = []
    for conf_level in confidence_levels:
        portfolio_returns_period = portfolio_returns * period  #assuming log returns over shorter periods are additive
        var = np.percentile(portfolio_returns_period, (1 - conf_level) * 100)
        var_row.append(var)
    var_results.append(var_row)

# summary dataframe
summary_data = pd.DataFrame(var_results, columns=[f'{int(conf * 100)}%' for conf in confidence_levels])
summary_data.insert(0, 'Holding Period', holding_periods)

# Add "day(s)" to Holding Period column for formatting
summary_data['Holding Period'] = summary_data['Holding Period'].apply(lambda x: f'{x} day(s)')

# Set the Confidence Level column as index for the summary dataframe
summary_data.set_index('Holding Period', inplace=True)

# Rename columns for clarity
summary_data.columns.name = 'Confidence Level'
print(var_results)
print(summary_data)

