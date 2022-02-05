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
            cars = db.execute('SELECT * FROM car WHERE car_id = ?', car_id).fetchone()

            result = [dict(cars)]

            if cars is None:
                return jsonify({"message": "Car by given ID does not exist", "status": 401})
            else:
                return jsonify({"cars": result, "status": 200})

        except db.IntegrityError:
            return jsonify({"message": "System error", "status": 401})
