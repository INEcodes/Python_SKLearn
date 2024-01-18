import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df =pd.read_csv("C:/Users/ADMIN/Documents/GitHub/Python-SKLearn/Iris_Flower_kaggle/IRIS.csv") 
fig, ax = plt.subplots(figsize=(10, 8))
sns.countplot(x='species',data=df,ax =ax)
plt.title("Iris species count")
plt.show()