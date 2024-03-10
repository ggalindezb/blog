from sqlite4 import SQLite4
from ..db import get_db

class UserModel:
    TABLE_NAME = "users"

    def __init__(self):
        self._id = None
        self._key = None
        self._created_on = None
        self._updated_on = None

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    @property
    def key(self):
        return self._key

    @key.setter
    def key(self, key):
        self._key = key

    @property
    def created_on(self):
        return self._created_on

    @created_on.setter
    def created_on(self, created_on):
        self._created_on = created_on

    @property
    def updated_on(self):
        return self._updated_on

    @updated_on.setter
    def updated_on(self, updated_on):
        self._updated_on = updated_on

    @classmethod
    def client(cls):
        db = SQLite4('blog/db/blog-db-dev')
        db.connect()
        return db

    @classmethod
    def find_by(cls, key=''):
        row = get_db().select(cls.TABLE_NAME, condition=f'key = "{key}"')[0]

        user = cls()
        user.id = row[0]
        user.key = row[1]
        user.created_on = row[2]
        user.updated_on = row[3]

        return user
