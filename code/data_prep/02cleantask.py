import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_excel(r"C:\Users\neves\OneDrive\Documents\TKH\real-state-pricing\data\raw\realestate.xlsx")

print(df.isna().sum())

rename_dict = {
    "X2 house age": "house_age", 
    "X3 distance to the nearest MRT station": "distance_to_mrt", 
    "X4 number of convenience stores": "num_convenience_stores",
    "X5 latitude": "lat",
    "X6 longitude": "long",
    "Y house price of unit area": "price_unit_area"
}

df_rename = df.rename(columns=rename_dict)


print(df_rename.columns)

#This variable defines the unwanted columns

selected = ["lat", "long", "No"]

#This redifines df to exclude the unwanted columns

df_drop = df_rename.drop(selected, axis=1)

print(df_drop)

df_drop["distance_to_mrt"] = df_drop["distance_to_mrt"].str.strip("\"").astype(float)


print(df_drop.shape)

df_drop = df_drop.dropna()

print(df_drop.shape)

print(df_drop.median())

print(df_drop.max())

print(df_drop.min())

print(df_drop.count())

df_outl = df_drop[df_drop.num_convenience_stores >= 0]

print(df_outl.shape)

df_outl = df_outl[df_outl.num_convenience_stores < 100]

print(df_outl.shape)

df_outl = df_outl[df_outl.house_age != 410.3]

print(df_outl.shape)

sns.histplot(df_outl["price_unit_area"])
plt.show()

sns.histplot(df_outl["house_age"])
plt.show()

sns.histplot(df_outl["num_convenience_stores"])
plt.show()

sns.histplot(df_outl["distance_to_mrt"])
plt.show()

sns.scatterplot(data=df_outl, x="price_unit_area", y="house_age")
plt.show()

sns.scatterplot(data=df_outl, x="price_unit_area", y="num_convenience_stores")
plt.show()

sns.scatterplot(data=df_outl, x="price_unit_area", y="distance_to_mrt")
plt.show()

mask = np.triu(np.ones_like(df_outl.corr(), dtype=np.bool_))

sns.heatmap(df_outl.corr(), annot=True, mask=mask)
plt.show()

df_drop.to_excel(r"C:\Users\neves\OneDrive\Documents\TKH\real-state-pricing\data\processed\tpdata.xlsx")

df_outl.to_excel(r"C:\Users\neves\OneDrive\Documents\TKH\real-state-pricing\data\processed\tp2data.xlsx")
