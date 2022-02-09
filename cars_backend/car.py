import functools
import random
import json
import decimal

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for, jsonify
)
from flask_cors import cross_origin

from cars_backend.db import get_db

bp = Blueprint("car", __name__, url_prefix="/car")


def dec_serializer(o):
    if isinstance(o, decimal.Decimal):
        return float(o)


@bp.route("/getAll", methods=["GET"])
@cross_origin()
def get_all_cars():
    if request.method == 'GET':
        db = get_db()

        try:
            cars = db.execute('SELECT * FROM car').fetchmany(12)

            result = []
            for row in cars:
                result.append(dict(row))
            # print(result[0]['price'])

            if cars is None:
                return jsonify({"message": "Cars database does not exist", "status": 401})
            else:
                return jsonify({"cars": result, "status": 200})

        except db.IntegrityError:
            return jsonify({"message": "System error", "status": 401})


@bp.route("/view/<car_id>", methods=["GET"])
@cross_origin()
def view_car(car_id):
    if request.method == 'GET':
        db = get_db()

        try:
            cars = db.execute('SELECT * FROM car WHERE car_id = ?', (car_id,)).fetchone()

            result = [dict(cars)]

            if cars is None:
                return jsonify({"message": "Car by given ID does not exist", "status": 401})
            else:
                return jsonify({"cars": result, "status": 200})

        except db.IntegrityError:
            return jsonify({"message": "System error", "status": 401})


@bp.route("/similar", methods=["GET"])
@cross_origin()
def find_similar():
    if request.method == 'GET':
        db = get_db()
        car_id = request.args.get("id")

        try:
            cars = db.execute('SELECT * FROM car WHERE car_id = ?', (car_id,)).fetchone()

            brand = cars["brand"]
            economy = float(cars["fuel_consumption"])
            mileage = int(cars["km_driven"])
            bhp = int(cars["max_power"])
            price = int(cars["price"])
            year = int(cars["year"])
            engine = float(cars["engine"])

            result = []

            # economical alternatives are: smaller engine, higher economy, similar year, similar price
            cars = db.execute('SELECT * FROM car WHERE engine < ? AND fuel_consumption > ? AND year >= ? AND price < ?', (engine, economy, year-2, price+5000)).fetchall()

            for row in cars:
                row = dict(row)
                row["suggestion_title"] = "Better Economy Alternative"
                row["suggestion_reason"] = "This car has a better economical footprint whilst being similar age and " \
                                           "price. These economic benefits would save you money on longer journeys."
                result.append(row)

            # value alternatives are: smaller price, lower mileage, similar year
            cars = db.execute('SELECT * FROM car WHERE price < ? AND km_driven < ? AND year >= ?', (price, mileage, year-1)).fetchall()

            for row in cars:
                row = dict(row)
                row["suggestion_title"] = "Better Value Alternative"
                row["suggestion_reason"] = "This car is cheaper with a similar mileage and age. Could be worth " \
                                           "consideration. "
                result.append(row)

            # performance alternatives are: higher engine, higher bhp, similar year, similar price
            cars = db.execute('SELECT * FROM car WHERE engine > ? AND max_power > ? AND year >= ? AND price < ?', (engine, bhp, year-2, price+5000)).fetchall()

            for row in cars:
                row = dict(row)
                row["suggestion_title"] = "Higher Performance Alternative"
                row["suggestion_reason"] = "This car offers much higher performance, with a higher top speed and" \
                                           " faster 0-60 time. Still around the same year and price. "
                result.append(row)

            # similar alternatives are: same brand, lower price, similar year
            cars = db.execute('SELECT * FROM car WHERE brand == ? AND price < ? AND year >= ?', (brand, price, year-2)).fetchall()

            for row in cars:
                row = dict(row)
                row["suggestion_title"] = "Similar Vehicle"
                row["suggestion_reason"] = "This car is very similar to the one being viewed, at a lower price."
                result.append(row)

            if len(result) > 2:
                result = random.sample(result, 2)

            if cars is None:
                return jsonify({"message": "Cars database does not exist", "status": 401})
            else:
                return jsonify({"cars": result, "status": 200})

        except db.IntegrityError:
            return jsonify({"message": "System error", "status": 401})
