from sqlite4 import SQLite4
from flask import current_app, g
from pymongo import MongoClient

def get_mongo_db():
    client = MongoClient()
    return client.blog

def get_db():
    if 'db' not in g:
        g.db = SQLite4(current_app.config['DATABASE'])
        g.db.connect()

    return g.db

def close_db(e=None):
    db = g.pop('db', None)

    # Enable this once ported out of SQLite4
    # if db is not None:
    #     db.close()
