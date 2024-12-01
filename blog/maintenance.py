from flask import Blueprint, jsonify

blueprint = Blueprint('maintenance', __name__, url_prefix='/maintenance')

@blueprint.route('/ping', methods=['GET'])
def ping():
    return (jsonify({ 'ping': True }), 200)
