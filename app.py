# importing flask module fro
import csv
import os

import flask
from flask import Flask, render_template, request, jsonify
from flaskext.mysql import MySQL
from preprocess import prepro, pic_prepro
from PIL import Image
from flask_cors import CORS, cross_origin
# import torch
# from fastai import *
# from fastai.vision import *
import requests  # for API example
import urllib.parse  # for API example

mysql = MySQL()

# initializing a variable of Flask
app = Flask(__name__)
cors = CORS(app)
class_names = []
with open('AI/names.csv', newline='') as Cars:
    cvsRead = csv.reader(Cars)
    for row in cvsRead:
        class_names.append(row[0])


@app.route('/api/usedCarPrice', methods=['POST'])
@cross_origin()
def useCarPrice():
    features = request.get_json()
    print(features)
    price = prepro(features)
    print("TESTING PRICE BEFORE RETURN")
    print(price)
    data = {'Price': price}
    return jsonify(data), 200

@app.route('/api/SearchCarAi', methods=['POST'])
def searchCarAI():
    picture = request.files['test']
    img = Image.open(picture)
    img.save("AI/Temp_pics/pics/prediction.png", "")
    print(picture)
    result = pic_prepro(img)
    print(class_names[result])
    os.remove("7047CEM/AI/Temp_pics/pics/prediction.png")
    return class_names[result]

if __name__ == "__main__":
    app.run(debug=True)
