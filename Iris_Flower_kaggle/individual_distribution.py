import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df =pd.read_csv("C:/Users/ADMIN/Documents/GitHub/Python-SKLearn/Iris_Flower_kaggle/IRIS.csv") 
g = sns.jointplot(x='sepal_length', y='sepal_width', data=df, kind="kde",color="m")
g.plot_joint(plt.scatter,c="b",s=40, linewidth=1, marker="+")
g.ax_joint.collections[0].set_alpha(0)
g.set_axis_labels("$SepalLenght$", "$SepalWidth$")
plt.show()