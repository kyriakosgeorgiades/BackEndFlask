"""
Creation of the machine learning model for price prediction
"""
import pickle
import warnings

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.ensemble import RandomForestRegressor
from sklearn.exceptions import DataConversionWarning
from sklearn.linear_model import Ridge
from sklearn.metrics import r2_score
from sklearn.model_selection import RandomizedSearchCV
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import OrdinalEncoder
# pylint: disable=E1101
# pylint: disable=E1136
# pylint: disable=E1137

warnings.filterwarnings("ignore", category=DataConversionWarning)

df = pd.read_csv('Car details v3.csv')
print(df.head())

# To understand the data types which are required to be transformed
print(df.info())

print(df.describe())

# Transforming the data
cars_used = df.copy(deep=True)
df['mileage'] = df['mileage'].str.extract(r'(\d+.\d+)').astype('float')
df['engine'] = df['engine'].str.extract('(^\\d*)')
df['max_power'] = df['max_power'].str.extract('(^\\d*)')
# Torque Extraction
df['torque'] = df['torque'].str.extract('(^\\d*)')
df['torque'] = df['torque'].fillna(150)
df['torque'] = df['torque'].astype(int)
# if it's in kgm, change it to N.m by multiplying by g= 9.8
df['torque'] = df['torque'].apply(lambda x: 9.8 * x if x <= 50 else x)

# Encoding the data
enc = OrdinalEncoder()
df["fuel"] = enc.fit_transform(df[["fuel"]])
df["seller_type"] = enc.fit_transform(df[["seller_type"]])
df["transmission"] = enc.fit_transform(df[["transmission"]])
df["owner"] = enc.fit_transform(df[["owner"]])
df["name"] = enc.fit_transform(df[["name"]])

df.dropna(inplace=True)
df['engine'] = df['engine'].astype(int)
df['max_power'] = df['max_power'].dropna()
df['max_power'].replace({'': 0}, inplace=True)
df['max_power'] = df['max_power'].astype(int)

print(df.corr().selling_price.sort_values().to_frame())

plt.subplots(figsize=(16, 10))
sns.heatmap(df.corr(), annot=True, cmap="RdBu")
plt.show()

print(df.head())

# Training and testing the model
x = df.drop(['selling_price', 'name'], axis=1)
y = df[['selling_price']]
X_train, X_test, y_train, y_test = train_test_split(
    x, y, test_size=0.2, random_state=25)
print("TRAINING")
print(X_train.to_string())
# Applying linear regression
lin_reg = Ridge()
lin_reg.fit(X_train, y_train)
y_pred = lin_reg.predict(X_test)
print(f"R2 Score for Linear Regression on test data: {np.round(r2_score(y_test,y_pred) ,3)}")

plt.scatter(y_test, y_pred)
plt.show()
n_estimators = []
max_depth = []
# Creating a list of range for the n_estimators for RandomSearch
for x in range(200, 2001, 200):
    n_estimators.append(x)
# Creating a list of range for max_depth for RandomSearch
for x in range(10, 101, 10):
    max_depth.append(x)

max_features = ['auto', 'sqrt']
bootstrap = [True, False]
random_grid = {'n_estimators': n_estimators,
               'max_features': max_features,
               'max_depth': max_depth,
               'bootstrap': bootstrap}

model = RandomForestRegressor()
tunning = RandomizedSearchCV(
    estimator=model,
    param_distributions=random_grid,
    n_iter=20,
    cv=10,
    verbose=2,
    random_state=36,
    n_jobs=-1)
# Fit the random search model
tunning.fit(X_train, y_train.values.ravel())
print(tunning.best_params_, tunning.best_score_)

model = RandomForestRegressor(**tunning.best_params_)
model.fit(X_train.values, y_train.values.ravel())

scores = cross_val_score(
    model,
    X_train.values,
    y_train.values,
    cv=5,
    scoring='r2')
print(f"R2 Score CV for RandomForest =  {(np.round(scores.mean(), 2))}")

y_pred = model.predict(X_train.values)
print(f"RandomForestRegressor results on train data: R2 Score: {(r2_score(y_train, y_pred))}")

y_pred = model.predict(X_test.values)
print(f"RandomForestRegressor results on train data: R2 Score: {(r2_score(y_test, y_pred))}")
plt.figure(figsize=(12, 8))
plt.scatter(y_test, y_pred)
plt.show()
print("Test price")
print(y_test)
print(y_pred[2])

FILENAME = "../user_car_perict.sav"
pickle.dump(model, open(FILENAME, 'wb'))


print(X_test.info())
print(X_test['seller_type'].unique())
print(X_test)
random_test = {
    "name": 123.0,
    "year": 2018,
    "km_driven": 236598,
    "fuel": 3.0,
    "seller_type": 1.0,
    "transmisssion": 1.0,
    "owner": 2.0,
    "mileage": 15.00,
    "engine": 1061,
    "max_power": 152,
    "torque": 88.0,
    "seats": 5.0}
print(random_test)
random_test = [123.0, 2018, 236598, 3.0, 1.0, 1.0,
               2.0, 15.00, 1061, 152, 88.0, 5.0]
random_test = [2015, 25000, 3.0, 1.0, 1.0,
               0.0, 17.01, 1591, 121, 154.0, 5.0]
# random_test = np.reshape(random_test, (1,-1)).T
random_test = np.reshape(random_test, (1, -1))
print(random_test)
print(model.predict(random_test))
print(x.head().to_string)
