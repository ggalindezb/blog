# Blog API

## Install

Load the SQLite database

```shell
sqlite3 db/blog-db-dev
```

```sql
.read db/schema.sql
.read db/seeds/development.sql
.schema
select * from posts;
select * from users;
```

Pull packages and start with:

```shell
pipenv install
pipenv shell
python app.py
```

Run `pipenv install` whenever packages change.

## Test

TBD

## Deploy

This will likely be hosted in a plain old tiny EC2 instance, perhaps serverless.
