# Import necessary libraries and modules
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score

import pandas as pd
import pickle

# Read the data from an Excel file into a pandas DataFrame
df = pd.read_excel(r"C:\Users\neves\OneDrive\Documents\TKH\real-state-pricing\data\processed\tp2data.xlsx")

# Split the data into features (X) and target (y)
X = df.drop('price_unit_area', axis=1) # Features (excluding 'price_unit_area')

y = df["price_unit_area"] # Target variable ('price_unit_area')

# Split the data into training and testing sets (75% training, 25% testing)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25)

# Create a Linear Regression model
reg = LinearRegression()

# Fit the model to the training data
reg.fit(X_train, y_train)

# Predict on the test set
y_pred = reg.predict(X_test)

# Calculate the R-squared score to evaluate the model's performance
r2 = r2_score(y_test, y_pred)

print("R^2:", r2)# Print the R-squared score


# Calculate the Mean Squared Error (MSE) to evaluate the model's performance
mse = mean_squared_error(y_test, y_pred)

print("MSE:", mse)# Print the Mean Squared Error

# Save the trained model using pickle for future use
pickle.dump(reg, open(r"C:\Users\neves\OneDrive\Documents\TKH\real-state-pricing\code\model\saved_models\linreg.sav", 'wb'))
