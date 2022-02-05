import functools
import random

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for, jsonify
)
from flask_cors import cross_origin

from cars_backend.db import get_db

bp = Blueprint("auth", __name__, url_prefix="/auth")


@bp.route("/register", methods=("GET", "POST"))
@cross_origin()
def register():
    if request.method == 'POST':
        data = request.get_json()
        first_name = data["first_name"]
        last_name = data["last_name"]
        email = data["email"]
        password = data["password"]

        db = get_db()
        error = None

        if not first_name:
            error = "First name is required."
        elif not last_name:
            error = "Last name is required."
        elif not email:
            error = "Email is required."
        elif not password:
            error = "Password is required."

        if error is None:
            try:
                letters = 'abcdefghijklmnopqrstuvwxyz@.'

                # Random Key Generation
                upperLetters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
                lowerLetters = 'abcdefghijklmnopqrstuvwxyz'
                numbers = '0123456789'

                character_bank = [upperLetters, lowerLetters, numbers]
                alphanumeric = ''.join(character_bank)

                generated = []
                for i in range(0, 32):
                    randomiser = random.choice(alphanumeric)
                    generated.append(randomiser)
                join = ''.join(generated)
                keyString = join

                # Random Salt Generation
                character_list = []
                for i in range(0, 16):
                    randomiser = random.choice(letters)
                    character_list.append(randomiser)
                salt = ''.join(character_list)

                # Combine Salt & Password
                combineSalt_password = [salt, password]
                joinCombine1 = ''.join(combineSalt_password)

                # Hashes the Password
                order = [letters.index(char.lower()) for char in joinCombine1]
                hashed_password = (''.join(keyString[alpha] for alpha in order))

                # Commits Registration Information To DB
                db.execute("INSERT INTO user (first_name, last_name, email, hash_key, salt, hashed_password) "
                           "VALUES (?, ?, ?, ?, ?, ?)",
                           (first_name, last_name, email, keyString, salt, hashed_password),
                           )
                db.commit()

            except db.IntegrityError:
                return jsonify({"message": "Email already registered", "status": 401})
            else:
                return jsonify({"message": "Registration successful", "status": 200})


@bp.route("/login", methods=("GET", "POST"))
@cross_origin()
def login():
    if request.method == "POST":
        data = request.get_json()
        email = data["email"]
        password = data["password"]

        db = get_db()

        user = db.execute(
            'SELECT * FROM user WHERE email = ?', (email,)
        ).fetchone()

        if user is None:
            return jsonify({"message": "Invalid credentials", "status": 401})

        letters = 'abcdefghijklmnopqrstuvwxyz@.'

        # Retrieve DB information
        database_hashed_password = user["hashed_password"]
        database_hash_key = user["hash_key"]
        database_salt = user["salt"]

        # Combines Salt & Password
        combineSalt_password = [database_salt, password]
        joinCombine1 = ''.join(combineSalt_password)

        # Hashes the Password
        order = [letters.index(char.lower()) for char in joinCombine1]
        hashed_password = (''.join(database_hash_key[alpha] for alpha in order))

        # Compares User Inputted Password to DB for Login
        if hashed_password == database_hashed_password:
            session.clear()
            session["user_id"] = user["user_id"]
            session["email"] = user["email"]
            return jsonify({"user_id": session["user_id"], "email": session["email"], "status": 200})
        else:
            return jsonify({"message": "Invalid credentials", "status": 401})


@bp.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("index"))


@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    else:
        g.user = get_db().execute(
            'SELECT * FROM user WHERE user_id = ?', (user_id,)
        ).fetchone()


def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for("auth.login"))

        return view(**kwargs)

    return wrapped_view
