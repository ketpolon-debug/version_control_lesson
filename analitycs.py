# import liblaries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# create dataFrame from dictionary
df = pd.DataFrame({'Name':['Ira', 'Mark', 'Ostap'], 'Age':[24, 31, 26]})
# print df.head()
print(df.head())
sns.barplot = sns.barplot(data = df, x = 'Name', y = 'Age')
plt.show()