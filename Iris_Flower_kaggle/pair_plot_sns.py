import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df =pd.read_csv("C:/Users/ADMIN/Documents/GitHub/Python-SKLearn/Iris_Flower_kaggle/IRIS.csv")
#df = df.drop('species',axis = 1)
sns.pairplot(df,hue='species')
plt.show()
