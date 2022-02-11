import csv
import os
import unittest
import pickle
import numpy as np
import pytest
from tensorflow.keras.applications.resnet50 import decode_predictions
from tensorflow.keras.preprocessing import image
from keras.engine.training_generator_v1 import predict_generator
from keras_preprocessing.image import ImageDataGenerator
import keras.models

# Cars image recognition setup
class_names = []
with open('../AI/names.csv', newline='') as Cars:
    cvs_read = csv.reader(Cars)
    for row in cvs_read:
        class_names.append(row[0])


@pytest.fixture
def data():
    return [2015, 25000, 3.0, 1.0, 1.0,
            0.0, 17.01, 1591, 121, 154.0, 5.0]


def test_input_types_price(data):
    array_check = []
    for i in data:
        if isinstance(i, int):
            array_check.append(0)
        elif isinstance(i, float):
            array_check.append(1)
    assert (array_check == [0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1])



def test_prediction_price(data):
    data = np.reshape(data, (1, -1))
    price = model.predict(data)
    assert price is not None


# Model expecting specific output since the input is known
def test_model_output():
    im = "test_pics/pics/prediction.jpg"
    pic = image.load_img(im, target_size=(224, 224))
    img_array = image.img_to_array(pic)
    img_batch = np.expand_dims(img_array, axis=0)
    car_is = model_picture.predict(img_batch)
    prediction = np.argmax(car_is[0])
    print(class_names[prediction])
    assert (class_names[prediction] == "BMW Z4 Convertible 2012")

def test_picture_exists():
    picture_status = os.path.exists("test_pics/pics/prediction.jpg")
    assert picture_status == True

model_picture = keras.models.load_model('../AI/final_version')
model = pickle.load(open('../user_car_perict.sav', 'rb'))
