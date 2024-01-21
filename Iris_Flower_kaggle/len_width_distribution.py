import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df =pd.read_csv("C:/Users/ADMIN/Documents/GitHub/Python-SKLearn/Iris_Flower_kaggle/IRIS.csv") 
new_data = df.drop("species",axis=1)
new_data.hist(edgecolor='black',linewidth=1.2)
fig = plt.gcf()
fig.set_size_inches(12,12)
fig1 = sns.jointplot(x='sepal_length', y ='sepal_width', data=df,color = 'blue')
fig2 = sns.jointplot(x='sepal_length', y ='sepal_width', data=df,color='red', kind="hex")
fig3 = sns.jointplot(x='sepal_length', y ='sepal_width', data=df,color='cyan', kind="kde")
fig4 = sns.jointplot(x='sepal_length', y ='sepal_width', data=df,color='red', kind="reg")
fig5 = sns.jointplot(x='sepal_length', y ='sepal_width', data=df,color='green').plot_joint(sns.kdeplot, zorder=0, n_levels=6)
plt.show()
