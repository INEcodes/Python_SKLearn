import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
df =pd.read_csv("C:/Users/ADMIN/Documents/GitHub/Python-SKLearn/Iris_Flower_kaggle/IRIS.csv")
X=df.iloc[:, 0:4]
f, ax = plt.subplots(figsize=(10,8))
corr = X.corr()
print(corr)
sns.heatmap(corr, mask = np.zeros_like(corr), cmap=sns.diverging_palette(220, 10, as_cmap=True), square=True,
            ax= ax, linewidths=.5)
plt.show()