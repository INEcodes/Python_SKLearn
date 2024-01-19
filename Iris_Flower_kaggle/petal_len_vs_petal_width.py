import pandas as pd
import matplotlib.pyplot as plt
df =pd.read_csv("C:/Users/ADMIN/Documents/GitHub/Python-SKLearn/Iris_Flower_kaggle/IRIS.csv")
fig = df[df.species=='Iris-setosa'].plot.scatter(x='petal_length',y='petal_width', color='orange', label='Setosa')
df[df.species=='Iris-versicolor'].plot.scatter(x='petal_length',y='petal_width', color='blue', label='versicolor',ax = fig)
df[df.species=='Iris-virginica'].plot.scatter(x='petal_length',y='petal_width', color='green', label='virginica', ax=fig)
fig.set_xlabel("Petal length")
fig.set_ylabel("Petal Width")
fig.set_title("Petal Length VS Width")
fig = plt.gcf()
fig.set_size_inches(12,8)
plt.show()