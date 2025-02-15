from flask import Blueprint, render_template, request
from blog.models.post_model import PostModel

blueprint = Blueprint('main', __name__, url_prefix='/')

@blueprint.route('/')
def fetch_blog():
    posts = PostModel.list()
    return render_template('posts.html.jinja', posts=posts)
