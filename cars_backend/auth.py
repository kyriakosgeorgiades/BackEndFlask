import functools, numpy, string

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

from cars_backend.db import get_db

bp = Blueprint("auth", __name__, url_prefix="/auth")


@bp.route("/register", methods=("GET", "POST"))
def register():
    if request.method == 'POST':
        first_name = request.form["first_name"]
        last_name = request.form["last_name"]
        email = request.form["email"]
        password = request.form["password"]

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
                db.execute(
                    "INSERT INTO user (first_name, last_name, email, hashed_password, salt) "
                    "VALUES (?, ?, ?, ?, 'test')",
                    (first_name, last_name, email, generate_password_hash(password)),
                )
                db.commit()
            except db.IntegrityError:
                error = f"User {first_name} is already registered."
            else:
                return redirect(url_for("auth.login"))

        flash(error)

    return render_template('auth/register.html')

''' Hashing Program for Registration Purposes '''
# Registration Hashing Program
@bp.route("/registerHash", method=("GET", "Post"))
def registerHash():
    letters = 'abcdefghijklmnopqrstuvwxyz@.'

    email = request.form["email"]
    password = request.form["password"]

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
    db.execute("INSERT INTO user (email, keyString, salt, hashed_password) "
               "VALUES (?, ?, ?, ?, 'test')",
                (email, keyString, salt, hashed_password),
    )
    db.commit()


''' Hashing Program for Login Purposes '''
@bp.route("/loginHash", method=("GET", "Post"))
def loginHash():

    ''' 'Retrieve DB Information' Needs to specifically get DB Info - Needs Update '''
    # Retrieve DB information 
    email = user_input_email
    password =user_input_password
    database_email = DB_email
    database_hashed_password = DB_hashed_password
    database_hash_key = DB_hash_key
    database_salt = DB_salt

    # Combines Salt & Password
    combineSalt_password = [database_salt, password]
    joinCombine1 = ''.join(combineSalt_password)

    # Hashs the Password
    order = [letters.index(char.lower()) for char in joinCombine1]
    hashed_password = (''.join(database_hash_key[alpha] for alpha in order))

    # Compares User Inputted Password to DB for Login
    if hashed_password == database_hashed_password:
        print("Login Successful", "\n")
        return "Login Accepted"
    if hashed_password != database_hashed_password:
        print("Login Unsuccessful", "\n")
        return "Login Failure"



@bp.route("/login", methods=("GET", "POST"))
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        print("Email: ", email)
        print("Password: ", password)

        db = get_db()
        error = None
        user = db.execute(
            'SELECT * FROM user WHERE email = ?', (email,)
        ).fetchone()

        print("User object: ", user)

        if user is None:
            error = "Incorrect username."
        elif not check_password_hash(user["hashed_password"], password):
            error = "Incorrect password."

        if error is None:
            session.clear()
            session["user_id"] = user["user_id"]
            return redirect(url_for("auth.login"))

        flash(error)

    return render_template("auth/login.html")


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
