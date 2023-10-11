
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score

import pandas as pd
import pickle

df = pd.read_excel(r"C:\Users\neves\OneDrive\Documents\TKH\real-state-pricing\data\processed\tp2data.xlsx")

# split data into "X" and "y" set
X = df.drop('price_unit_area', axis=1)
y = df["price_unit_area"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25)

reg = LinearRegression()

reg.fit(X_train, y_train)

# Predict on the test set
y_pred = reg.predict(X_test)

# Calculate score
r2 = r2_score(y_test, y_pred)

print("R^2:", r2)

mse = mean_squared_error(y_test, y_pred)

print("MSE:", mse)

pickle.dump(reg, open(r"C:\Users\neves\OneDrive\Documents\TKH\real-state-pricing\code\model\saved_models\linreg.sav", 'wb'))
