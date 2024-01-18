import pandas as pd
import matplotlib.pyplot as plt
df =pd.read_csv("C:/Users/ADMIN/Documents/GitHub/Python-SKLearn/Iris_Flower_kaggle/IRIS.csv") 
df.describe().plot(kind='area', fontsize=16, figsize=(15,8), table=True, colormap="Accent")
plt.xlabel('Statistics')
plt.ylabel('Value')
plt.title("General Statistics of Iris Dataset")
plt.show()

fig, ax = plt.subplots(figsize=(10,8))
df['species'].value_counts().plot.pie(explode=[0.1,0.1,0.1], autopct='%1.1f%%', shadow=True, figsize=(10,8))
plt.title("Iris Species %")
plt.show()