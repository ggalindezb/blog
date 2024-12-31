from blog.models.post_model import PostModel
from datetime import datetime, timedelta
from bson.objectid import ObjectId
from unittest.mock import patch, MagicMock

def test_build_post():
    now = datetime.now() - timedelta(minutes=2)
    doc = {
      '_id': ObjectId('67723cecfc75dbb91fb1226f'),
      'slug': 'sample',
      'content': '<h1>Sample title</h1><p>Sample brief</p>',
      'created_on': now,
      'updated_on': now
    }
    post = PostModel.build_post(doc)

    assert post
    assert post.id, 1
    assert post.slug, 'sample'
    assert post.title, 'Sample title'
    assert post.brief, 'Sample brief'
    assert post.created_on, now
    assert post.updated_on, now

def test_build_post_with_none():
    post = PostModel.build_post(None)
    assert post is None

@patch('blog.models.post_model.get_mongo_db')
def test_find(mock_get_mongo_db):
    now = datetime.now() - timedelta(minutes=2)
    mock_collection = MagicMock()
    mock_get_mongo_db.return_value.posts = mock_collection

    mock_collection.find_one.return_value = {
      '_id': ObjectId('67723cecfc75dbb91fb1226f'),
      'slug': 'sample',
      'content': '<h1>Sample title</h1><p>Sample brief</p>',
      'created_on': now,
      'updated_on': now
    }

    post = PostModel.find({'slug': 'sample'})

    assert post
    assert post.slug, 'sample'
    assert post.title, 'Sample title'
    assert post.brief, 'Sample brief'

@patch('blog.models.post_model.get_mongo_db')
def test_list(mock_get_mongo_db):
    now = datetime.now() - timedelta(minutes=2)
    mock_collection = MagicMock()
    mock_get_mongo_db.return_value.posts = mock_collection

    mock_collection.find.return_value = [
        {
            '_id': ObjectId('67723cecfc75dbb91fb1226f'),
            'slug': 'sample',
            'content': '<h1>Sample title</h1><p>Sample brief</p>',
            'created_on': now,
            'updated_on': now
        }
    ]

    posts = list(PostModel.list())
    post = posts[0]

    assert len(posts) == 1
    assert post
    assert post.slug, 'sample'
    assert post.title, 'Sample title'
    assert post.brief, 'Sample brief'

@patch('blog.models.post_model.get_mongo_db')
def test_create(mock_get_mongo_db):
    mock_collection = MagicMock()
    mock_get_mongo_db.return_value.posts = mock_collection

    slug = 'sample'
    content = '<h1>Sample title</h1><p>Sample brief</p>'
    now = datetime.now()

    with patch("blog.models.post_model.datetime") as mock_datetime:
        mock_datetime.now.return_value = now
        PostModel.create(slug, content)

    mock_collection.insert_one.assert_called_once_with(
        {
            'slug': slug,
            'content': content,
            'created_on': now,
            'updated_on': now,
        }
    )

@patch("blog.models.post_model.get_mongo_db")
def test_update(mock_get_mongo_db):
    mock_collection = MagicMock()
    mock_get_mongo_db.return_value.posts = mock_collection

    slug = 'test-slug'
    content = '<h1>Updated Title</h1><p>Updated Brief</p>'
    now = datetime.now()

    with patch('blog.models.post_model.datetime') as mock_datetime:
        mock_datetime.now.return_value = now
        PostModel.update(slug, content)

    mock_collection.update_one.assert_called_once_with(
        {'slug': slug},
        {'$set': {'updated_on': now, 'content': content}},
    )

@patch("blog.models.post_model.get_mongo_db")
def test_delete(mock_get_mongo_db):
    mock_collection = MagicMock()
    mock_get_mongo_db.return_value.posts = mock_collection

    slug = 'sample'
    PostModel.delete(slug)

    mock_collection.delete_one.assert_called_once_with({'slug': slug})
