from flask import Flask
from dotenv import load_dotenv
from werkzeug.middleware.proxy_fix import ProxyFix
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
        APP_ENV=os.environ['APP_ENV']
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

    if app.config['APP_ENV'] == 'production':
        app.wsgi_app = ProxyFix(
            app.wsgi_app, x_for=1, x_proto=1, x_host=1, x_prefix=1
        )

    return app
