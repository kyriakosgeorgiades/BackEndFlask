''' Hashing Program for Registration Purposes '''

import numpy, pandas, csv, string, functools
from cars_backend.db import get_db

from flask import (Blueprint, flash, g, redirect, render_template, request, session, url_for)

# Registration Hashing Program
@bp.route("/register", method=("GET", "POST"))
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
@bp.route("/login", method=("GET", "POST"))
def login():

    email = request.form["email"]
    password = request.form["password"]
    
    db.execute("SELECT * FROM (email, keyString, salt, hashed_password) "
               "VALUES (?, ?, ?, ?, 'test')",
                (email, keyString, salt, hashed_password),
    )
    
    # Retrieve DB information 
    user_email = email
    user_password = password
    database_hashed_password = hashed_password
    database_hash_key = keyString
    database_salt = salt

    # Combines Salt & Password
    combineSalt_password = [database_salt, user_password]
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
