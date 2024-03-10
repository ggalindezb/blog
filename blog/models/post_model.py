from datetime import datetime
from sqlite4 import SQLite4
from bs4 import BeautifulSoup
from ..db import get_db

class PostModel:
    TABLE_NAME = "posts"

    def __init__(self):
        self._id = None
        self._slug = None
        self._title = None
        self._brief = None
        self._content = None
        self._created_on = None
        self._updated_on = None

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
    def title(self):
        return self._title

    @title.setter
    def title(self, content):
        parser = BeautifulSoup(content, 'html.parser')
        self._title = parser.h1.string

    @property
    def brief(self):
        return self._brief

    @brief.setter
    def brief(self, brief):
        self._brief = brief.decode('utf-8')

    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, content):
        self._content = content.decode('utf-8')

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
    def build_post(cls, row):
        if not row:
            return None

        post = cls()
        post.id = row[0]
        post.slug = row[1]
        post.content = row[2]
        post.title = post.content
        post.created_on = row[3]
        post.updated_on = row[4]

        return post

    @classmethod
    def find_by(cls, slug=''):
        rows = get_db().select(cls.TABLE_NAME, condition=f'slug = "{slug}"')
        if rows:
            return cls.build_post(rows[0])

    @classmethod
    def list(cls, page=1):
        rows = get_db().select(cls.TABLE_NAME)
        return map(cls.build_post, rows)

    def create(self, slug, content):
        now = datetime.now()
        get_db().insert(self.TABLE_NAME, {"slug": slug, "content": content, "created_on": now, "updated_on": now})

    def find(self, slug):
        return get_db().select(self.TABLE_NAME, condition=f'slug = "{slug}"')

    def update(self, slug, content):
        now = datetime.now()
        return get_db().update(self.TABLE_NAME, {"content": content}, f'slug ="{slug}"')

    def delete(self, slug):
        return get_db().delete(self.TABLE_NAME, f'slug ="{slug}"')
