import pandas as pd  
df = pd.read_csv("C:/Users/ADMIN/Documents/GitHub/Python-SKLearn/Iris_Flower_kaggle/IRIS.csv")  
#print(df)
print(df.shape)
#print(df.head(3))
print(df.keys())
print(df.info())
print(df.describe())
print(f"Observation of each species:{df['species'].value_counts()}")


