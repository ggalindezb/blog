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
sqlite3 blog-db-dev
```

```.sql
.read db.sql
.schema
select * from posts;
select * from users;
```
