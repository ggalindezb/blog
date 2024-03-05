from flask import Flask, render_template, request, jsonify
from services.auth import generate_token, validate_token
from models.post_model import PostModel
from models.user_model import UserModel

app = Flask(__name__)

@app.route('/login', methods=['POST'])
def login():
    key = request.get_json()['key']
    user = UserModel.find_by(key)
    token = generate_token(user)
    return jsonify({"jwt": token})

@app.route('/posts')
def fetch_posts():
    posts = PostModel.list()
    return render_template('posts.html.jinja', posts=posts)

@app.route('/posts/<slug>')
def fetch_post(slug):
    post = PostModel.find_by(slug)
    return render_template('post.html', post=post)

@app.route('/posts', methods=['POST'])
@validate_token
def create_post():
    slug = request.get_json()['slug']
    content = request.get_json()['content']
    posts = PostModel()
    posts.create(slug, content)
    return ('', 201)

@app.route('/posts/<slug>', methods=['PUT'])
@validate_token
def update_post(slug):
    content = request.get_json()['content']
    posts = PostModel()
    posts.update(slug, content)
    return ('', 200)

@app.route('/posts/<slug>', methods=['DELETE'])
@validate_token
def delete_post(slug):
    posts = PostModel()
    posts.delete(slug)
    return ('', 200)

if __name__ == '__main__':
    app.run(debug=True)
