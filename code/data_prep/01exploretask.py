# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Read data from an Excel file into a pandas DataFrame
df = pd.read_excel(r"C:\Users\neves\OneDrive\Documents\TKH\real-state-pricing\data\raw\realestate.xlsx")

# Print the first 5 rows of the DataFrame
print(df.head(5))

# Print a concise summary of the DataFrame, including column information
print(df.info(verbose=True))

# Generate descriptive statistics for numerical columns in the DataFrame
print(df.describe(include=[np.number]))

# Create a histogram for the 'Y house price of unit area' column
sns.histplot(df["Y house price of unit area"])
plt.show()

# Create a boxplot for the 'Y house price of unit area' column
sns.boxplot(df["Y house price of unit area"])
plt.show()

# Create a histogram for the 'X2 house age' column
sns.histplot(df["X2 house age"])
plt.show()

# Create a boxplot for the 'X2 house age' column
sns.boxplot(df["X2 house age"])
plt.show()

# Create a histogram for the 'X4 number of convenience stores' column
sns.histplot(df["X4 number of convenience stores"])
plt.show()

# Create a boxplot for the 'X4 number of convenience stores' column
sns.boxplot(df["X4 number of convenience stores"])
plt.show()

# Create a scatter plot for 'X2 house age' vs 'Y house price of unit area'
sns.scatterplot(data=df, x="X2 house age", y="Y house price of unit area")
plt.show()

# Create a scatter plot for 'X4 number of convenience stores' vs 'Y house price of unit area'
sns.scatterplot(data=df, x="X4 number of convenience stores", y="Y house price of unit area")
plt.show()

# Select specific columns for correlation analysis
selected_cols = ["X2 house age", "X4 number of convenience stores", "Y house price of unit area"]

# Create a mask for the upper triangle of the correlation heatmap
mask = np.triu(np.ones_like(df[selected_cols].corr(), dtype=np.bool_))

# Create a correlation heatmap for the selected columns
sns.heatmap(df[selected_cols].corr(), annot=True, mask=mask)
plt.show()