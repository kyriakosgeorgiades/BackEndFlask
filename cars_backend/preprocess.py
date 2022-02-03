
import pickle
import keras.models
import sklearn
import numpy as np
from keras.engine.training_generator_v1 import predict_generator
from keras_preprocessing.image import ImageDataGenerator
from sklearn.preprocessing import OrdinalEncoder
import pandas as pd


def prepro(features):
    # Loading the model
    model = pickle.load(open('user_car_perict.sav', 'rb'))
    data = []
    df = pd.json_normalize(features)
    enc = OrdinalEncoder()
    df["fuel"] = enc.fit_transform(df[["fuel"]])
    df["seller_type"] = enc.fit_transform(df[["seller_type"]])
    df["transmission"] = enc.fit_transform(df[["transmission"]])
    df["owner"] = enc.fit_transform(df[["owner"]])
    # features['fuel'] = enc.fit_transform(np.reshape(features['fuel'], (1, -1)))
    for key, value in df.items():
        data.append(value)
    data = np.reshape(data, (1, -1))
    price = model.predict(data)
    price = price * 0.0099
    val = np.float32(price)
    price = val.item()
    price = int(round(price))
    print("THIS IS THE PRICE")
    print(price)
    return price


def pic_prepro(pic):
    model = keras.models.load_model('AI/final_version')
    # picture = image.load_img('AI/Temp_pics/prediction.png', target_size=(224, 224))
    # img_array = image.img_to_array(picture)
    # img_batch = np.expand_dims(img_array, axis=0)
    # img_preprocessed = preprocess_input(img_batch)
    # car_is = model.predict(img_preprocessed)
    # prediction = np.argmax(car_is[0])
    train_datagen = ImageDataGenerator(

    )
    train = train_datagen.flow_from_directory(
        'AI/Temp_pics/',
        class_mode='categorical',
        target_size=(224, 224),
        batch_size=1,
        shuffle=False
    )
    prediction = model.predict_generator(train,  verbose=1)
    cl = np.round(prediction)
    prediction = np.argmax(cl[0])
    # pic = image.smart_resize(pic, (224, 224))
    # img_array = image.img_to_array(pic)
    # img_batch = np.expand_dims(img_array, axis=0)
    # fix = np.array(img_batch).copy()
    # img_preprocessed = preprocess_input(fix)
    # car_class = model.predict(img_preprocessed)
    # prediction = np.argmax(car_class[0])
    return prediction

