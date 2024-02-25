# Blog API

## Install

Pull packages and start with:

```shell
pipenv install
pipenv shell
python app.py
```

Load the SQLite database

```shell
sqlite3 db/blog-db-dev
```

```.sql
.read db/schema.sql
.read db/seeds/development.sql
.schema
select * from posts;
select * from users;
```
