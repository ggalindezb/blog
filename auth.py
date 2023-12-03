import jwt
import os
import functools
import flask
import pdb

JWT_TOKEN = os.environ['JWT_TOKEN']

def generate_token(secret):
    return jwt.encode({'user_id': secret}, JWT_TOKEN, algorithm='HS256')

def validate_token(token):
    return jwt.decode(token, JWT_TOKEN, algorithm='HS256')

def wrapper(request):
    print('Outside')
    print(request)
    def inner(func):
        print('Wrapper')
        return func
    return inner

def validate_request(f):
    @functools.wraps(f)
    def decorated_function(*args, **kwargs):
        try:
            bearer_token = flask.request.headers['Authorization'].split().pop()
            jwt.decode(bearer_token, JWT_TOKEN, algorithms=['HS256'])
        except KeyError:
            flask.abort(401)
        return f(*args, **kwargs)
    return decorated_function
