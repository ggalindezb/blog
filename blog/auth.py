from flask import Blueprint, request, jsonify
from blog.models.user_model import UserModel
from blog.services.auth import generate_token

blueprint = Blueprint('auth', __name__, url_prefix='/auth')

@blueprint.route('/login', methods=['POST'])
def login():
    key = request.get_json()['key']
    user = UserModel.find({'key': key})
    token = generate_token(user)
    return jsonify({'jwt': token})
