from datetime import datetime
from sqlite4 import SQLite4
from bs4 import BeautifulSoup
from ..db import get_db, get_mongo_db

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
    def content(self):
        return self._content

    @content.setter
    def content(self, content):
        self._content = content

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
    def brief(self, content):
        parser = BeautifulSoup(content, 'html.parser')
        self._brief = parser.p.string

    @classmethod
    def build_post(cls, doc):
        if not doc:
            return None

        post = cls()

        for key, value in doc.items():
            setattr(post, key, value)

        post.title = post.content
        post.brief = post.content

        return post

    @classmethod
    def find(cls, params):
        doc = get_mongo_db().posts.find_one(params)
        return cls.build_post(doc)

    @classmethod
    def list(cls, page=1):
        docs = get_mongo_db().posts.find({})
        return map(cls.build_post, docs)

    def create(self, slug, content):
        now = datetime.now()
        get_db().insert(self.TABLE_NAME, {"slug": slug, "content": content, "created_on": now, "updated_on": now})

    def update(self, slug, content):
        now = datetime.now()
        return get_db().update(self.TABLE_NAME, {"content": content}, f'slug ="{slug}"')

    def delete(self, slug):
        return get_db().delete(self.TABLE_NAME, f'slug ="{slug}"')
