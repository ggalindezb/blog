from sqlite4 import SQLite4

import click
from flask import current_app, g

def get_db():
    if 'db' not in g:
        g.db = SQLite4('blog/db/blog-db-dev')
        g.db.connect()

    return g.db

def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()
