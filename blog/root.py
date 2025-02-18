from flask import Blueprint, render_template, jsonify
from blog.models.post_model import PostModel

blueprint = Blueprint('root', __name__, url_prefix='/')

@blueprint.route('/')
def fetch_root():
    posts = PostModel.list()
    return render_template('posts.html.jinja', posts=posts)

@blueprint.route('/ping', methods=['GET'])
def ping():
    return (jsonify({ 'ping': True }), 200)
