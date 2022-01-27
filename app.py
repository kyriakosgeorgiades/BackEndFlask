# importing flask module fro
import flask
from flask import Flask, render_template, request, jsonify
from flaskext.mysql import MySQL
from preprocess import prepro
import requests  # for API example
import urllib.parse  # for API example

mysql = MySQL()

# initializing a variable of Flask
app = Flask(__name__)


@app.route('/api/usedCarPrice', methods=['POST'])
def useCarPrice():
    features = request.get_json()
    print(features)
    price = prepro(features)
    print("TESTING PRICE BEFORE RETURN")
    print(price)
    data = {'Price': price}
    return jsonify(data), 200


if __name__ == "__main__":
    app.run(debug=True)
