from flask import current_app, g
from pymongo import MongoClient

def get_mongo_db():
    return MongoClient().blog

def close_db(__exception__):
    mongo_db = g.pop('mongo_db', None)

    if mongo_db is not None:
        mongo_db.close()
