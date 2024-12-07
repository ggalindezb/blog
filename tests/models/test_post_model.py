from blog.models.post_model import PostModel
from datetime import datetime

def test_build_post():
    row = [1, 'sample', b'<h1>Sample title</h1><p>Sample brief</p>', datetime.now(), datetime.now()]
    post = PostModel.build_post(row)

    assert post
    assert post.id, 1
    assert post.slug, 'sample'
    assert post.title, 'Sample title'
    assert post.brief, 'Sample brief'
