from datetime import datetime
from sqlite4 import SQLite4

class PostModel:
    TABLE_NAME = "posts"

    def __init__(self) -> None:
        self.db = SQLite4('blog-db-dev')
        self.db.connect()

    def all(self):
        return self.db.select(self.TABLE_NAME)

    def create(self, slug, content):
        now = datetime.now()
        self.db.insert(self.TABLE_NAME, {"slug": slug, "content": content, "created_on": now, "updated_on": now})

    def find(self, slug):
        return self.db.select(self.TABLE_NAME, condition=f'slug = "{slug}"')
