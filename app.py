from flask import Flask, request
from post_model import PostModel
import auth

app = Flask(__name__)

@app.route("/login", methods=["POST"])
def login():
    secret = int(request.get_json()['secret'])
    token = auth.generate_token(secret)
    return {"jwt": token}

@app.route("/posts")
@auth.validate_request
def fetch_posts():
    posts = PostModel()
    return posts.all()

@app.route("/posts", methods=["POST"])
def create_post():
    slug = request.get_json()['slug']
    content = request.get_json()['content']
    posts = PostModel()
    posts.create(slug, content)
    return ('', 201)

@app.route("/posts/<slug>")
def fetch_post(slug):
    posts = PostModel()
    return posts.find(slug)

@app.route("/posts/<slug>", methods=["PUT"])
def update_post(slug):
    content = request.get_json()['content']
    posts = PostModel()
    posts.update(slug, content)
    return ('', 200)

@app.route("/posts/<slug>", methods=["DELETE"])
def delete_post(slug):
    posts = PostModel()
    posts.delete(slug)
    return ('', 200)

if __name__ == "__main__":
    app.run()
