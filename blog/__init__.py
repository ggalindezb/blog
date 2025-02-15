from flask import Flask
from dotenv import load_dotenv
import os

from . import db
from . import maintenance
from . import main
from . import posts
from . import auth

def create_app(test_config=None):
    load_dotenv()
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY=os.environ['SECRET_KEY'],
        DATABASE=os.environ['DATABASE'],
    )

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    app.register_blueprint(maintenance.blueprint)
    app.register_blueprint(auth.blueprint)
    app.register_blueprint(main.blueprint)
    app.register_blueprint(posts.blueprint)
    # app.teardown_appcontext(db.close_db)

    return app
