import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df =pd.read_csv("C:/Users/ADMIN/Documents/GitHub/Python-SKLearn/Iris_Flower_kaggle/IRIS.csv") 
ax=plt.subplot(1,1,figsize=(10,8))
sns.countplot('Species',data=df)
plt.title("Iris species count")
plt.show()