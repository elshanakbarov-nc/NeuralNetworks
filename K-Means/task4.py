import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sklearn
from sklearn.metrics import mean_squared_error
import math
from math import sqrt

data = pd.read_csv("Book.csv")

feature_columns = ['A', 'B']
X = data[feature_columns]
y = data['C']
# from sklearn.model_selection import train_test_split
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 1, random_state = 0)


from sklearn import neighbors


x_test = [[3.7,45]]

model = neighbors.KNeighborsRegressor(n_neighbors=4)
model.fit(X, y)
y_pred = model.predict(x_test)
print(y_pred)

