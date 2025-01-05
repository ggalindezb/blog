const fs = require('fs')

db = connect( 'mongodb://localhost/blog' );
db.getCollectionNames().forEach(collection => db[collection].deleteMany({}))
db.dropDatabase({})

db.users.insertMany(
  [
    {
      key: '2a1e0fc0-7bab-4aa0-9e2f-23d7ddd81241',
      created_on: '2024-12-01 00:00:00',
      updated_on: '2024-12-01 00:00:00'
    }
  ]
)

db.posts.insertMany(
  [
    {
      slug: 'test',
      content: fs.readFileSync('blog/db/seeds/posts/test.html', 'utf8'),
      featured_image: 'img/featured/1.jpg',
      gradient: ['#eb6050', '#ba3c1c'],
      created_on: '2024-12-01 01:00:00',
      updated_on: '2024-12-01 01:00:00'
    },
    {
      slug: 'a-better-terminal-experience',
      content: fs.readFileSync('blog/db/seeds/posts/a.html', 'utf8'),
      featured_image: 'img/featured/2.jpg',
      gradient: ['#cd6e42', '#b63521'],
      created_on: '2024-12-02 01:00:00',
      updated_on: '2024-12-02 01:00:00'
    },
    {
      slug: 'high-fiber-diet',
      content: fs.readFileSync('blog/db/seeds/posts/b.html', 'utf8'),
      featured_image: 'img/featured/3.jpg',
      gradient: ['#9ec6da', '#3c53ad'],
      created_on: '2024-12-03 01:00:00',
      updated_on: '2024-12-03 01:00:00'
    },
    {
      slug: 'leaf-compost',
      content: fs.readFileSync('blog/db/seeds/posts/c.html', 'utf8'),
      featured_image: 'img/featured/4.jpg',
      gradient: ['#babd7b', '#6a8760'],
      created_on: '2024-12-04 01:00:00',
      updated_on: '2024-12-04 01:00:00'
    },
    {
      slug: 'minimal-blog-with-flask-and-html',
      content: fs.readFileSync('blog/db/seeds/posts/d.html', 'utf8'),
      gradient: ['#e2944b', '#efc974'],
      featured_image: 'img/featured/5.jpg',
      created_on: '2024-12-05 01:00:00',
      updated_on: '2024-12-05 01:00:00'
    }
  ]
)
