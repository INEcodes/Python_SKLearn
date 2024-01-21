import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df =pd.read_csv("C:/Users/ADMIN/Documents/GitHub/Python-SKLearn/Iris_Flower_kaggle/IRIS.csv")
box_data = df
box_target = df.species
sns.boxplot(data=box_data, width=0.5, fliersize=5)
sns.set(rc={'figure.figsize':(2, 15)})
plt.show()