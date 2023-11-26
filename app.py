from flask import Flask, request
from sqlite4 import SQLite4
from post_model import PostModel

app = Flask(__name__)

@app.route("/posts")
def fetch_posts():
    posts = PostModel()
    return posts.all()

@app.route("/posts", methods=["POST"])
def create_post():
    posts = PostModel()
    posts.create('test', 'Test content')
    return request.get_json()

@app.route("/posts/<slug>")
def fetch_post(slug):
    posts = PostModel()
    return posts.find(slug)

if __name__ == "__main__":
    app.run(debug=True)
