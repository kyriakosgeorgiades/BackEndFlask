import pickle
import warnings
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


from sklearn.preprocessing import OrdinalEncoder
from sklearn.model_selection import RandomizedSearchCV
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.linear_model import Ridge
from sklearn.ensemble import RandomForestRegressor

from sklearn.exceptions import DataConversionWarning

warnings.filterwarnings("ignore", category=DataConversionWarning)

df = pd.read_csv('Car details v3.csv')
print(df.head())

# To understand the data types which are required to be transfomred
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
lin_reg = Ridge()
lin_reg.fit(X_train, y_train)
y_pred = lin_reg.predict(X_test)
print(
    'R2 Score for Linear Regression on test data: {}'.format(
        np.round(
            r2_score(
                y_test,
                y_pred),
            3)))

plt.scatter(y_test, y_pred)
plt.show()

n_estimators = [int(x) for x in np.linspace(start=200, stop=2000, num=10)]
max_features = ['auto', 'sqrt']
max_depth = [int(x) for x in np.linspace(10, 100, num=10)]
bootstrap = [True, False]
random_grid = {'n_estimators': n_estimators,
               'max_features': max_features,
               'max_depth': max_depth,
               'bootstrap': bootstrap}

rf = RandomForestRegressor()
rf_random = RandomizedSearchCV(
    estimator=rf,
    param_distributions=random_grid,
    n_iter=20,
    cv=3,
    verbose=2,
    random_state=42,
    n_jobs=-1)
# Fit the random search model
rf_random.fit(X_train, y_train)
print(rf_random.best_params_, rf_random.best_score_)

rf = RandomForestRegressor(**rf_random.best_params_)
rf.fit(X_train.values, y_train.values)

scores = cross_val_score(
    rf,
    X_train.values,
    y_train.values,
    cv=5,
    scoring='r2')
print('R2 Score CV for RandomForest = {}'.format(np.round(scores.mean(), 2)))

y_pred = rf.predict(X_train.values)
print(
    'RandomForestRegressor results on train data: R2 Score: {}  - MSE Score: {}'.format(
        r2_score(
            y_train, y_pred), mean_squared_error(
            y_train, y_pred)))

y_pred = rf.predict(X_test.values)
print(
    'RandomForestRegressor results on train data: R2 Score: {}  - MSE Score: {}'.format(
        r2_score(
            y_test, y_pred), mean_squared_error(
            y_test, y_pred)))
plt.figure(figsize=(12, 8))
plt.scatter(y_test, y_pred)
plt.show()
print("I AM PRICE OF FIRST TEST")
print(y_test)
print(y_pred[2])

FILENAME = "../user_car_perict.sav"
pickle.dump(rf, open(FILENAME, 'wb'))

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
print(rf.predict(random_test))
print(x.head().to_string)
