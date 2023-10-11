# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Read data from an Excel file into a pandas DataFrame
df = pd.read_excel(r"C:\Users\neves\OneDrive\Documents\TKH\real-state-pricing\data\raw\realestate.xlsx")

# Print the count of missing values in each column
print(df.isna().sum())

# Rename columns using a dictionary
rename_dict = {
    "X2 house age": "house_age", 
    "X3 distance to the nearest MRT station": "distance_to_mrt", 
    "X4 number of convenience stores": "num_convenience_stores",
    "X5 latitude": "lat",
    "X6 longitude": "long",
    "Y house price of unit area": "price_unit_area"
}

# Rename columns in the DataFrame
df_rename = df.rename(columns=rename_dict)

# Print the columns of the renamed DataFrame
print(df_rename.columns)

# Define a list of unwanted columns
selected = ["lat", "long", "No"]

# Exclude unwanted columns from the DataFrame
df_drop = df_rename.drop(selected, axis=1)

# Strip quotes and convert 'distance_to_mrt' to float
df_drop["distance_to_mrt"] = df_drop["distance_to_mrt"].str.strip("\"").astype(float)

# Print the shape of the DataFrame
print(df_drop.shape)

# Drop rows with any missing values
df_drop = df_drop.dropna()

# Print the shape of the DataFrame after dropping missing values
print(df_drop.shape)

# Print the median, max, min, and count for each column
print(df_drop.median())
print(df_drop.max())
print(df_drop.min())
print(df_drop.count())

# Filter rows based on a condition for 'num_convenience_stores'
df_outl = df_drop[df_drop.num_convenience_stores >= 0]

# Filter rows based on a condition for 'num_convenience_stores'
df_outl = df_outl[df_outl.num_convenience_stores < 100]

# Filter rows based on a condition for 'house_age'
df_outl = df_outl[df_outl.house_age != 410.3]

# Create histograms for specific columns
sns.histplot(df_outl["price_unit_area"])
plt.show()

sns.histplot(df_outl["house_age"])
plt.show()

sns.histplot(df_outl["num_convenience_stores"])
plt.show()

sns.histplot(df_outl["distance_to_mrt"])
plt.show()

# Create scatter plots for specific columns
sns.scatterplot(data=df_outl, x="price_unit_area", y="house_age")
plt.show()

sns.scatterplot(data=df_outl, x="price_unit_area", y="num_convenience_stores")
plt.show()

sns.scatterplot(data=df_outl, x="price_unit_area", y="distance_to_mrt")
plt.show()

# Create a heatmap for the correlation matrix of the DataFrame
mask = np.triu(np.ones_like(df_outl.corr(), dtype=np.bool_))
sns.heatmap(df_outl.corr(), annot=True, mask=mask)
plt.show()

# Save the processed DataFrame to an Excel file
df_outl.to_excel(r"C:\Users\neves\OneDrive\Documents\TKH\real-state-pricing\data\processed\tp2data.xlsx")
