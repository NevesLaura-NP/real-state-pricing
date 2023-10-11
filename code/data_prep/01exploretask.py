import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_excel(r"C:\Users\neves\OneDrive\Documents\TKH\real-state-pricing\data\raw\realestate.xlsx")

#
print(df.head(5))

print(df.info(verbose=True))

print(df.describe(include=[np.number]))

sns.histplot(df["Y house price of unit area"])
plt.show()

sns.boxplot(df["Y house price of unit area"])
plt.show()

sns.histplot(df["X2 house age"])
plt.show()

sns.boxplot(df["X2 house age"])
plt.show()

sns.histplot(df["X4 number of convenience stores"])
plt.show()

sns.boxplot(df["X4 number of convenience stores"])
plt.show()

sns.scatterplot(data=df, x="X2 house age", y="Y house price of unit area")
plt.show()

sns.scatterplot(data=df, x="X4 number of convenience stores", y="Y house price of unit area")
plt.show()

selected_cols = ["X2 house age", "X4 number of convenience stores", "Y house price of unit area"]

mask = np.triu(np.ones_like(df[selected_cols].corr(), dtype=np.bool_))

sns.heatmap(df[selected_cols].corr(), annot=True, mask=mask)
plt.show()


