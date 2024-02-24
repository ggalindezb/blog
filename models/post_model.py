from datetime import datetime
from sqlite4 import SQLite4

class PostModel:
    TABLE_NAME = "posts"

    def __init__(self):
        self._id = None
        self._slug = None
        self._content = None
        self._created_on = None
        self._updated_on = None

    def __init__(self) -> None:
        self.db = SQLite4('blog-db-dev')
        self.db.connect()

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    @property
    def slug(self):
        return self._slug

    @slug.setter
    def slug(self, slug):
        self._slug = slug

    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, content):
        self._slug = content

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
        db = SQLite4('blog-db-dev')
        db.connect()
        return db

    @classmethod
    def find_by(cls, slug=''):
        db = cls.client()
        row = db.select(cls.TABLE_NAME, condition=f'slug = "{slug}"')[0]

        post  = cls()
        post.id = row[0]
        post.slug = row[1]
        post.content = row[2]
        post.created_on = row[3]
        post.updated_on = row[4]

        return post

    def all(self):
        return self.db.select(self.TABLE_NAME)

    def create(self, slug, content):
        now = datetime.now()
        self.db.insert(self.TABLE_NAME, {"slug": slug, "content": content, "created_on": now, "updated_on": now})

    def find(self, slug):
        return self.db.select(self.TABLE_NAME, condition=f'slug = "{slug}"')

    def update(self, slug, content):
        now = datetime.now()
        return self.db.update(self.TABLE_NAME, {"content": content}, f'slug ="{slug}"')

    def delete(self, slug):
        return self.db.delete(self.TABLE_NAME, f'slug ="{slug}"')
