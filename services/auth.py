import jwt
import os
import functools
import flask
from flask import request, g

JWT_TOKEN = os.environ['JWT_TOKEN']

def generate_token(user):
    return jwt.encode({'user_id': user.id}, JWT_TOKEN, algorithm='HS256')

def validate_token(f):
    @functools.wraps(f)
    def token_validation(*args, **kwargs):
        try:
            bearer_token = request.headers['Authorization'].split().pop()
            token = jwt.decode(bearer_token, JWT_TOKEN, algorithms=['HS256'])
            g.token = token
        except KeyError:
            flask.abort(401)
        return f(*args, **kwargs)
    return token_validation
