import csv
import functools
import os

from PIL import Image
from flask import (
    Blueprint, flash, g, request, session, url_for, jsonify
)
from werkzeug.security import check_password_hash, generate_password_hash
from flask_cors import CORS, cross_origin
from cars_backend.preprocess import prepro, pic_prepro
from cars_backend.db import get_db

bp = Blueprint("api", __name__, url_prefix="/api")

# Cars image recognition setup
class_names = []
with open('AI/names.csv', newline='') as Cars:
    cvs_read = csv.reader(Cars)
    for row in cvs_read:
        class_names.append(row[0])


@bp.route("/usedCarPrice", methods=["POST"])
@cross_origin()
def used_car_price():
    try:
        features = request.get_json()
        print("Car features: ", features)
        price = prepro(features)
        print("Predicted price: ", price)
        data = {'Price': price}
        return jsonify(data), 200
    except:
        return "Missing Value", 404


@bp.route('/searchCarAI', methods=['POST'])
def search_car_ai():
    picture = request.files['file']
    img = Image.open(picture)
    img.save("AI/Temp_pics/pics/prediction.png")
    print(picture)
    result = pic_prepro(img)
    print(class_names[result])
    os.remove("AI/Temp_pics/pics/prediction.png")
    return class_names[result]
