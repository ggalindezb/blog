from flask import Blueprint, render_template, request
from blog.models.post_model import PostModel
from blog.services.auth import validate_token

blueprint = Blueprint('posts', __name__, url_prefix='/posts')

@blueprint.route('/')
def fetch_posts():
    posts = PostModel.list()
    return render_template('posts.html.jinja', posts=posts)

@blueprint.route('<slug>')
def fetch_post(slug):
    post = PostModel.find({'slug': slug})
    return render_template('post.html', post=post)

@blueprint.route('/', methods=['POST'])
@validate_token
def create_post():
    slug = request.get_json()['slug']
    content = request.get_json()['content']
    PostModel.create(slug, content)
    return ('', 201)

@blueprint.route('<slug>', methods=['PUT'])
@validate_token
def update_post(slug):
    content = request.get_json()['content']
    PostModel.update(slug, content)
    return ('', 200)

@blueprint.route('<slug>', methods=['DELETE'])
@validate_token
def delete_post(slug):
    posts = PostModel()
    posts.delete(slug)
    return ('', 200)
