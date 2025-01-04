from ..db import get_mongo_db

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
    def build_user(cls, doc):
        if not doc:
            return None

        user = cls()
        doc['id'] = doc.pop('_id')
        for key, value in doc.items():
            setattr(user, key, value)

        return user

    @classmethod
    def find(cls, params):
        doc = get_mongo_db().users.find_one(params)
        return cls.build_user(doc)
