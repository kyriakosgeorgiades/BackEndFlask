"""
Provides routes for AI related functionalities
"""
import csv
import os

from PIL import Image
from flask import (
    Blueprint, request, jsonify
)
from flask_cors import cross_origin
from cars_backend.preprocess import prepro, pic_prepro

bp = Blueprint("api", __name__, url_prefix="/api")

# Cars image recognition setup
# Loading the classes name to a local variable
# to be used with in the route of the car classification
class_names = []
with open('AI/names.csv', newline='', encoding='UTF-8') as Cars:
    cvs_read = csv.reader(Cars)
    for row in cvs_read:
        class_names.append(row[0])


@bp.route("/usedCarPrice", methods=["POST"])
@cross_origin()
def used_car_price():
    """ Route for predicting the price of the car based on input features
    :
     :returns
     (data, status_code):
        Returning json data of the predicted price
        The status code of the response
    :except
    (err, status_code):
        Returning the error raised
        The status code of the response
     """
    try:
        features = request.get_json()
        print("Car features: ", features)
        # Calling the function to preprocess the data for the prediction
        price = prepro(features)
        print("Predicted price: ", price)
        data = {'Price': price}
        # Creating a json data for the response
        data = jsonify(data)
        status_code = 200
        return data, status_code
    except TypeError as err:
        print(err)
        status_code = 500
        return jsonify(str(err)), status_code
    except ValueError as err:
        status_code = 500
        return jsonify(str(err)), status_code


@bp.route('/searchCarAI', methods=['POST'])
def search_car_ai():
    """ Route for predicting the car model and brand from an input picture
    :
     :returns
     (data, status_code):
        Returning json data of the predicted car picture
        The status code of the response
    :except
    (Exception, status_code):
        Returning the error raised
        The status code of the response
    """
    try:
        picture = request.files['file']
        img = Image.open(picture)
        # Storing the picture to a temporary directory
        img.save("AI/Temp_pics/pics/prediction.png")
        print(picture)
        # Function call for preprocessing the picture and prediction
        result = pic_prepro()
        print(class_names[result])
        # Removing the picture from the temporary directory
        os.remove("AI/Temp_pics/pics/prediction.png")
        status_code = 200
        data = class_names[result]
        return data, status_code
    except IOError as err:
        print(err)
        status_code = 500
        return jsonify(str(err)), status_code


