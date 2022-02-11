"""
Pre-processing functionalities of AI models
"""
import pickle

import keras.models
import numpy as np
import pandas as pd
from keras_preprocessing.image import ImageDataGenerator
from sklearn.preprocessing import OrdinalEncoder


def prepro(features):
    """
    Return the predicted price for a used car to be sold

        Parameters:
                features (list): All the features required for the prediction

        Returns:
                price (float): The predicted price of the used car

    """
    # Loading the model
    # Loading the machine learning model for prediction
    model = pickle.load(open('user_car_perict.sav', 'rb'))
    data = []
    # Normalize semi-structured JSOn data into a flat table
    df_ = pd.json_normalize(features)
    enc = OrdinalEncoder()  # Encode categorical features as an integer array
    # Transforming Fuel to numeric
    df_["fuel"] = enc.fit_transform(df_[["fuel"]])
    # Transforming Seller Type to numeric
    df_["seller_type"] = enc.fit_transform(df_[["seller_type"]])
    # Transforming Transmission to numeric
    df_["transmission"] = enc.fit_transform(df_[["transmission"]])
    # Transforming Owner to numeric
    df_["owner"] = enc.fit_transform(df_[["owner"]])
    for key, value in df_.items():
        data.append(value)
    # Reshaping the list to meet the model input criteria
    data = np.reshape(data, (1, -1))
    price = model.predict(data)
    price = price * 0.0099  # Covert the money from Indian rupees to British Pounds
    val = np.float32(price)
    price = val.item()
    price = int(round(price))
    return price


def pic_prepro():
    """
    Return the predicted index of the car

        Returns:
                prediction (int): The index that will match the class names list

    """
    # Loading the model
    model = keras.models.load_model('AI/final_version')
    # Initialing ImageDataGenerator object
    predict_datagen = ImageDataGenerator()
    # Preprocess happens in the prediction as it was a pretrain Resnet50 model
    # combined with the new connected layers
    predict = predict_datagen.flow_from_directory(
        'AI/Temp_pics/',
        class_mode='categorical',
        target_size=(224, 224),
        batch_size=1,
        shuffle=False
    )
    # Prediction
    prediction = model.predict_generator(predict, verbose=1)
    # Return highest probability of prediction
    prediction = np.argmax(prediction[0])
    return prediction
