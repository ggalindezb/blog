from flask import Blueprint, render_template, request
from blog.db import get_db
from blog.models.post_model import PostModel
from blog.services.auth import validate_token

blueprint = Blueprint('posts', __name__, url_prefix='/posts')

@blueprint.route('/all')
def fetch_posts():
    posts = PostModel.list()
    return render_template('posts.html.jinja', posts=posts)

@blueprint.route('<slug>')
def fetch_post(slug):
    post = PostModel.find_by(slug)
    return render_template('post.html', post=post)

@blueprint.route('/', methods=['POST'])
@validate_token
def create_post():
    slug = request.get_json()['slug']
    content = request.get_json()['content']
    posts = PostModel()
    posts.create(slug, content)
    return ('', 201)
