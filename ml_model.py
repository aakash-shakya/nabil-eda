import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt
import seaborn as sns
import pickle as pkl


df = pd.read_csv('nepsealpha_export_price_NABIL_2013-01-26_2023-01-26.csv')

ml_features = ['Open', 'High', 'Low']
ml_target = ['Close']

X = df[ml_features]
y = df[ml_target]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

regressor = LinearRegression()
model = regressor.fit(X_train, y_train)


pkl.dump(model, open('model.pkl', 'wb'))

y_pred = regressor.predict(X_test)

def regression_results(y_true, y_pred):
    # Regression metrics
    explained_variance=round(r2_score(y_test, y_pred), 2)
    mse=round(mean_squared_error(y_test, y_pred), 2)
    rmse=round(np.sqrt(mean_squared_error(y_test, y_pred)), 2)
    r2=round(r2_score(y_test, y_pred), 2)

    print('explained_variance: ', explained_variance)
    print('mse: ', mse)
    print('rmse: ', rmse)
    print('r2: ', r2)


regression_results(y_test, y_pred)

def predict_closing_price(open, high, low):
    close_price = regressor.predict([[open, high, low]])
    return close_price


print(predict_closing_price(1000, 1100, 950))


