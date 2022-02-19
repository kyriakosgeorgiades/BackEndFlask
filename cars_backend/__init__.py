# This is the entry point to the app and contains initialization code

import os
from flask import Flask


def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'cars_db.sqlite'),
    )

    # Create an instance folder if it doesn't exist. This will store the SQLite database.
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # Connect app to database
    from . import db
    db.init_app(app)

    # Register blueprints (which contain routes) to the app
    from . import auth
    app.register_blueprint(auth.bp)

    from . import api
    app.register_blueprint(api.bp)

    from . import car
    app.register_blueprint(car.bp)

    return app
