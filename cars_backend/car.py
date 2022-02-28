import random

from flask import (
    Blueprint, request, jsonify
)
from flask_cors import cross_origin
from googleapiclient.errors import HttpError

from cars_backend import youtube_api
from cars_backend.db import get_db

bp = Blueprint("car", __name__, url_prefix="/car")


@bp.route("/getAll", methods=["GET"])
@cross_origin()
def get_all_cars():
    """ Route called to return all car records
        returns: JSON list of cars and status code
        exception: JSON error message and status code
    """
    if request.method == 'GET':
        # connects with database
        db = get_db()

        try:
            # select all car info from database
            cars = db.execute('SELECT * FROM car').fetchmany(12)

            # adds result rows returned from sql query to list
            result = []
            for row in cars:
                result.append(dict(row))

            # if no car database has no records
            if cars is None:
                return jsonify({"message": "Cars database does not exist", "status": 401})
            else:
                return jsonify({"cars": result, "status": 200})

        # returns error code and message if exception occurs
        except db.IntegrityError:
            return jsonify({"message": "Database processing error", "status": 401})


@bp.route("/getID", methods=["POST"])
@cross_origin()
def get_name():
    """ Route for predicting getting the ID of a car by brand and name
    :
     :returns
     (car["car_id"], status):
        Returning json data of ID of the car
        The status code of the response
    :except
    (Exception, status_code):
        Returning the error raised
        The status code of the response
    """
    db = get_db()
    try:
        brand_name = request.form['name']
        # Breaking down the string
        brand_name = brand_name.split(" ", 1)
        # Brand of the car broken down from the string
        brand = brand_name[0]
        size = len(brand_name[1])
        # Model broken down from the string
        model = brand_name[1][:size - 5]
        # Query to fetch the ID of the car to be returned
        car = db.execute('SELECT car_id FROM car WHERE brand = ? AND model = ?', (brand, model)).fetchone()

        return jsonify({"ID": car["car_id"], "status": 200})

    except IndexError:
        return jsonify({"message": "System error", "status": 401})
    except db.IntegrityError:
        return jsonify({"message": "System error", "status": 401})


@bp.route("/view/<car_id>", methods=["GET"])
@cross_origin()
def view_car(car_id):
    """ Route called to view a single car by ID
        returns: JSON cars info dictionary and status code
        exception: JSON error message and status code
    """
    if request.method == 'GET':
        # connects with database
        db = get_db()

        try:
            # select car record by ID from database
            cars = db.execute('SELECT * FROM car WHERE car_id = ?', (car_id,)).fetchone()

            # stores the record as a dictionary list
            result = [dict(cars)]

            # if no car database has no records
            if cars is None:
                return jsonify({"message": "Car by given ID does not exist", "status": 401})
            else:
                # Call the API to find a video of the car
                try:
                    video_link = youtube_api.find_car_video(result[0])
                except HttpError as e:
                    print("An HTTP error %d occurred:\n%s" % (e.resp.status, e.content))
                else:
                    warranty = "Warranty offer: 14 months long for £450"
                    return jsonify({"cars": result, "video_link": video_link, "warranty": warranty, "status": 200})

        # returns error code and message if exception occurs
        except db.IntegrityError:
            return jsonify({"message": "System error", "status": 401})


@bp.route("/similar", methods=["GET"])
@cross_origin()
def find_similar():
    """ Route called to view similar cars of car by ID
        returns: JSON 2 cars list and status code
        exception: JSON error message and status code
    """
    if request.method == 'GET':
        # connects with database
        db = get_db()
        # gets the id from parameters
        car_id = request.args.get("id")

        try:
            # select car record by ID from database
            cars = db.execute('SELECT * FROM car WHERE car_id = ?', (car_id,)).fetchone()

            # stores returned car info as local variables
            brand = cars["brand"]
            economy = float(cars["fuel_consumption"])
            mileage = int(cars["km_driven"])
            bhp = int(cars["max_power"])
            price = int(cars["price"])
            year = int(cars["year"])
            engine = float(cars["engine"])

            # defines empty result list
            result = []

            # economical alternatives are: smaller engine, higher economy, similar year, similar price
            cars = db.execute('SELECT * FROM car WHERE engine < ? AND fuel_consumption > ? AND year >= ? AND price < ?',
                              (engine, economy, year - 2, price + 5000)).fetchall()

            # for returned rows from SQL query, appends extra info and adds to result list
            for row in cars:
                row = dict(row)
                row["suggestion_title"] = "Better Economy Alternative"
                row["suggestion_reason"] = "This car has a better economical footprint whilst being similar age and " \
                                           "price. These economic benefits would save you money on longer journeys."
                result.append(row)

            # value alternatives are: smaller price, lower mileage, similar year
            cars = db.execute('SELECT * FROM car WHERE price < ? AND km_driven < ? AND year >= ?',
                              (price, mileage, year - 1)).fetchall()

            # for returned rows from SQL query, appends extra info and adds to result list
            for row in cars:
                row = dict(row)
                row["suggestion_title"] = "Better Value Alternative"
                row["suggestion_reason"] = "This car is cheaper with a similar mileage and age. Could be worth " \
                                           "consideration. "
                result.append(row)

            # performance alternatives are: higher engine, higher bhp, similar year, similar price
            cars = db.execute('SELECT * FROM car WHERE engine > ? AND max_power > ? AND year >= ? AND price < ?',
                              (engine, bhp, year - 2, price + 5000)).fetchall()

            # for returned rows from SQL query, appends extra info and adds to result list
            for row in cars:
                row = dict(row)
                row["suggestion_title"] = "Higher Performance Alternative"
                row["suggestion_reason"] = "This car offers much higher performance, with a higher top speed and" \
                                           " faster 0-60 time. Still around the same year and price. "
                result.append(row)

            # similar alternatives are: same brand, lower price, similar year
            cars = db.execute('SELECT * FROM car WHERE brand == ? AND price < ? AND year >= ?',
                              (brand, price, year - 2)).fetchall()

            # for returned rows from SQL query, appends extra info and adds to result list
            for row in cars:
                row = dict(row)
                row["suggestion_title"] = "Similar Vehicle"
                row["suggestion_reason"] = "This car is very similar to the one being viewed, at a lower price."
                result.append(row)

            # if more than 2 results within list, takes 2 random samples to return
            if len(result) > 2:
                result = random.sample(result, 2)

            # if no car database has no records
            if cars is None:
                return jsonify({"message": "Cars database does not exist", "status": 401})
            else:
                return jsonify({"cars": result, "status": 200})

        # returns error code and message if exception occurs
        except db.IntegrityError:
            return jsonify({"message": "System error", "status": 401})
