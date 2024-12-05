use blog;
const fs = require('fs');

db.posts.insertMany(
  [
    {
      slug: 'test',
      title: 'Test',
      content: fs.readFileSync('blog/db/seeds/posts/test.html', 'utf8'),
      tags: ['test'],
      published: false,
      created_on: '2024-12-01 01:00:00',
      updated_on: '2024-12-01 01:00:00'
    },
    {
      slug: 'a-better-terminal-experience',
      title: 'A better terminal experience',
      content: fs.readFileSync('blog/db/seeds/posts/a.html', 'utf8'),
      tags: ['cli'],
      published: true,
      created_on: '2024-12-02 01:00:00',
      updated_on: '2024-12-02 01:00:00'
    },
    {
      slug: 'high-fiber-diet',
      title: 'High fiber diet',
      content: fs.readFileSync('blog/db/seeds/posts/b.html', 'utf8'),
      tags: ['nutrition'],
      published: false,
      created_on: '2024-12-03 01:00:00',
      updated_on: '2024-12-03 01:00:00'
    },
    {
      slug: 'leaf-compost',
      title: 'Leaf compost',
      content: fs.readFileSync('blog/db/seeds/posts/c.html', 'utf8'),
      tags: ['recycle', 'plants'],
      published: false,
      created_on: '2024-12-04 01:00:00',
      updated_on: '2024-12-04 01:00:00'
    },
    {
      slug: 'minimal-blog-with-flask-and-html',
      title: 'Minimal blog with flask and html',
      content: fs.readFileSync('blog/db/seeds/posts/d.html', 'utf8'),
      tags: ['python', 'flask', 'htmx'],
      published: true,
      created_on: '2024-12-05 01:00:00',
      updated_on: '2024-12-05 01:00:00'
    }
  ]
)
