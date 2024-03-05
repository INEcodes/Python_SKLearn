import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style('whitegrid')
plt.style.use("fivethirtyeight")


from pandas_datareader.data import DataReader
import yfinance as yf
from pandas_datareader import data as pdr

yf.pdr_override()

from datetime import datetime

tech_list = ['AAPL', 'GOOG', 'MSFT', 'AMZN']

tech_list = ['AAPL', 'GOOG', 'MSFT', 'AMZN']

end = datetime.now()
start = datetime(end.year -1, end.month, end.day-1)

for stock in tech_list:
    globals() [stock] = yf.download(stock, start, end)

company_list = [AAPL, GOOG, MSFT, AMZN]
company_name = ["APPLE", "GOOGLE", "MICROSOFT", "AMAZOn"]

for company, com_name in zip(company_list, company_name):
    company["company_name"] = com_name
    
df=pd.concat(company_list, axis = 0)
print(df.tail(10))

#correlation
closing_df = pdr.get_data_yahoo(tech_list, start=start, end = end)['Adj Close']

tech_rets = closing_df.pct_change()
tech_rets.head()

sns.jointplot(x='GOOG', y='GOOG', data=tech_rets, kind='scatter', color='seagreen')
plt.show()

sns.jointplot(x = 'GOOG', y = 'MSFT', data=tech_rets, kind = 'scatter')

sns.pairplot(tech_rets, kind='reg')

#set up our figure by naming it return_fig, call Pairplot on the dataframe
return_fig = sns.PairGrid(tech_rets.dropna())

#using map_upper we can specify what the upper triangle will look like
return_fig.map_upper(plt.scatter, color='purple')

#We can also define the lower triangle in the figure, including the plot type(kde)
#or the color map (BluePurple)
return_fig.map_lower(sns.kdeplot, cmap='cool_d')

#Finally we'll define the diagonal as a series of histogram plots of the daily return
return_fig.map_diag(plt.hist, bins=30)

#heatmap part
plt.figure(figsize=(12,10))
plt.subplot(2,2,1)
sns.heatmap(tech_rets.corr(), annot=True, cmap='summer')
plt.title('Correlation of stock return')

plt.subplot(2,2,2)
sns.heatmap(closing_df.corr(), annot=True, cmap = 'summer')
plt.title('Correlation of stock closing price')
plt.show()