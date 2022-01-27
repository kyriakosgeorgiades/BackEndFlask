import pickle
import sklearn
import numpy as np
from sklearn.preprocessing import OrdinalEncoder
import pandas as pd


def prepro(features):
    # Loading the model
    model = pickle.load(open('user_car_perict.sav', 'rb'))
    data = []
    df = pd.json_normalize(features)
    print(df.head())
    enc = OrdinalEncoder()
    df["fuel"] = enc.fit_transform(df[["fuel"]])
    df["seller_type"] = enc.fit_transform(df[["seller_type"]])
    df["transmission"] = enc.fit_transform(df[["transmission"]])
    df["owner"] = enc.fit_transform(df[["owner"]])
    features['fuel'] = enc.fit_transform(np.reshape(features['fuel'], (1, -1)))
    for key, value in df.items():
        data.append(value)
    data = np.reshape(data, (1, -1))
    price = model.predict(data)
    price = price * 0.0099
    val = np.float32(price)
    price = val.item()
    price = round(price, 2)
    print("THIS IS THE PRICE")
    print(price)
    return price
