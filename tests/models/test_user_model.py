from blog.models.user_model import UserModel
from datetime import datetime, timedelta
from bson.objectid import ObjectId
from unittest.mock import patch, MagicMock

def test_build_user():
    now = datetime.now() - timedelta(minutes=2)
    doc = {
      '_id': ObjectId('6778aeb7158425295d932ef3'),
      'key': '2a1e0fc0-7bab-4aa0-9e2f-23d7ddd81241',
      'created_on': now,
      'updated_on': now
    }
    user = UserModel.build_user(doc)

    assert user
    assert user.id == ObjectId('6778aeb7158425295d932ef3')
    assert user.key == '2a1e0fc0-7bab-4aa0-9e2f-23d7ddd81241'
    assert user.created_on == now
    assert user.updated_on == now

def test_build_user_with_none():
    user = UserModel.build_user(None)
    assert user is None
