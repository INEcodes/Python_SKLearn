#This includes the Machine Learning and other were the part of data analysis or data visualization

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn import decomposition
from sklearn import preprocessing
df =pd.read_csv("C:/Users/ADMIN/Documents/GitHub/Python-SKLearn/Iris_Flower_kaggle/IRIS.csv") 
le = preprocessing.LabelEncoder()
df.species = le.fit_transform(df.species)

X=df.iloc[:, :-1].values
Y=df.iloc[:, 4].values
fig = plt.figure(1, figsize=(7,6))
plt.clf()
ax=plt.axes(projection ='3d')
plt.cla()
pca = decomposition.PCA(n_components=3)
pca.fit(X)
X =pca.transform(X)

for name, label in [('Setosa', 0), ('Versicolour',1),('Virginica',2)]:
    ax.text3D(X[Y==label, 0].mean(),
              X[Y==label, 1].mean() + 1.5,
              X[Y==label, 2].mean(), name,
              horizontalalignment='center',
              bbox=dict(alpha=.5, edgecolor='w', facecolor='w'))
    
Y = np.choose(Y,[1, 2, 0])
ax.scatter(X[:, 0], X[:, 1], X[:, 2], c=Y, cmap=plt.cm.nipy_spectral, edgecolor='k')

ax.xaxis.set_ticklabels([])
ax.yaxis.set_ticklabels([])
ax.zaxis.set_ticklabels([])
plt.show()
