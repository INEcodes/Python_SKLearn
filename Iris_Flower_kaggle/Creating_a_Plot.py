import pandas as pd
import matplotlib.pyplot as plt
df =pd.read_csv("C:/Users/ADMIN/Documents/GitHub/Python-SKLearn/Iris_Flower_kaggle/IRIS.csv") 
df.describe().plot(kind='area', fontsize=16, figsize=(15,8), ) 