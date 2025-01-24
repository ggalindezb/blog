# Blog API

## Install

Install MongoDB, start the service and load seed data.

```sh
sudo systemctl start mongod
mongosh --file blog/db/seeds/seeds.js
```

Pull packages and start with:

```sh
pip install pipenv
pipenv install
pipenv shell
flask --app blog run --debug
```

Run `pipenv install` whenever packages change.

## Test

Run tests with `pytest`.

Check coverage with `coverage run -m pytest && coverage html && open htmlcov/index.html`

## Mongosh

A few useful commands so I don't forget.

```js
db.getCollectionNames()
db.blog.posts.find({})
db.blog.posts.deleteMany({})
```

## Deploy

This will likely be hosted in a plain old tiny EC2 instance, perhaps serverless.

### Docker build

```sh
pipenv requirements > requirements.txt
docker build . --tag blog
docker run --network host -ti blog
```
