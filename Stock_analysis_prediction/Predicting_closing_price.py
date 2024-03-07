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

df = pdr.get_data_yahoo('AAPL', start='2012-01-01', end = datetime.now())
df

plt.figure(figsize=(16,6))
plt.title('Close Price Histroy')
plt.plot(df['Close'])
plt.xlabel('Date', fontsize=18)
plt.xlabel('Close Price USD($)', fontsize=18)
plt.show()

#create a new dataframe with only the 'Close column
data = df.filter(['Close'])

#Convert the dataframe to a numpy array
dataset = data.values
#get the number of rows to train the model on
training_data_len = int(np.ceil(len(dataset) * 0.95))

#making of the training dataset
training_data_len

from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler(feature_range=(0,1))
scaled_data = scaler.fit_transform(dataset)

scaled_data


#create the training data set
#create the scaled training data set
train_data = scaled_data[0:int(training_data_len), :]
#split the data into x_train and y_train data sets
x_train = []
y_train = []

for i in range(60, len(train_data)):
    x_train.append(train_data[i-60:i, 0])
    y_train.append(train_data[i,0])
    
    if i<=61:
        print(x_train)
        print(y_train)
        
#Convert the x_train and y_train to numpy arrays:

x_train, y_train = np.array(x_train), np.array(y_train)

#Reshape the data:
x_train = np.reshape(x_train, (x_train.shape[0], x_train.shape[1], 1))
#x_train.shape
#for ML models we will be using Keras as it is a programmer friendly for the beginners in Deep Neural Networks(DNNs).

from keras.models import Sequential
from keras.layers import Dense, LSTM

model = Sequential()
model.add(LSTM(128, return_sequences = True, input_shape = (x_train.shape[1], 1)))
model.add(LSTM(64, return_sequences=False))
model.add(Dense(25))
model.add(Dense(1))

model.compile(optimizer='adam', loss='mean_squared_error')

model.fit(x_train, y_train, batch_size=1, epochs=1)


#Create the test dataset:
#Creating a new array containing scaled values from index 1543 to 2002

test_data = scaled_data[training_data_len - 60:, :]

x_test = []

y_test = dataset[training_data_len:,:]
for i in range(60, len(test_data)):
    x_test.append(test_data[i-60:i, 0])
    
x_test = np.array(x_test)

x_test = np.reshape(x_test, (x_test.shape[0], x_test.shape[1], 1))

# To get prediction from the ML models
predictions = model.predict(x_test)
predictions = scaler.inverse.transform(predictions)

#get the root mean squared error
rmse = np.sqrt(np.mean(((predictions - y_test) ** 2)))
print(rmse)

train = data[:training_data_len]
valid = data[training_data_len:]
valid['Predictions'] = predictions
#visualize the data
plt.figure(figsize=(16,6))
plt.title('Model')
plt.xlabel('Date', fontsize=18)
plt.ylabel('Close Price USD($)', fontsize=18)
plt.plot(train['Close'])
plt.plot(valid[['Close', 'Predictions']])
plt.legend(['Train', 'Val','Predictions'], loc='lower right')
plt.show()

print(valid)