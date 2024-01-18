import pandas as pd
import matplotlib.pyplot as plt
df =pd.read_csv("C:/Users/ADMIN/Documents/GitHub/Python-SKLearn/Iris_Flower_kaggle/IRIS.csv")
fig = df[df.species=='Iris-setosa'].plot(kind='scatter',x='sepal_length',y='sepal_width',color='orange',label='Setosa')
df[df.species=='Iris-versicolor'].plot(kind='scatter',x='sepal_length',y='sepal_width',color='blue',label='versicolor',ax=fig)
df[df.species=='Iris-virginica'].plot(kind='scatter',x='sepal_length',y='sepal_width',color='green',label='virginica',ax=fig)

fig.set_xlabel("Sepal Lenght")
fig.set_ylabel("Sepal Width")
fig.set_title("Sepal Length VS Width")
fig=plt.gcf()
fig.set_size_inches(12,8)
plt.show()
