import unittest
import pickle
import numpy as np
import pytest


@pytest.fixture
def data():
    return [2015, 25000, 3.0, 1.0, 1.0,
            0.0, 17.01, 1591, 121, 154.0, 5.0]


def test_input_types(data):
    array_check = []
    for i in data:
        if isinstance(i, int):
            array_check.append(0)
        elif isinstance(i, float):
            array_check.append(1)
    assert (array_check == [0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1])


def test_prediction(data):
    data = np.reshape(data, (1, -1))
    price = model.predict(data)
    price = int(price[0])
    price = price * 0.0099
    assert int(price) == 6967


model = pickle.load(open('../user_car_perict.sav', 'rb'))

random_test = [2015, 25000, 3.0, 1.0, 1.0,

               0.0, 17.01, 1591, 121, 154.0, 5.0]

test_input_types(random_test)
