-- Users
INSERT INTO users(key, created_on, updated_on)
VALUES('2a1e0fc0-7bab-4aa0-9e2f-23d7ddd81241', strftime('%Y-%m-%d %H:%M:%S', datetime('now')), strftime('%Y-%m-%d %H:%M:%S', datetime('now')));

-- Posts
INSERT INTO posts(slug, content, created_on, updated_on)
VALUES('a-better-terminal-experience', readfile('blog/db/seeds/posts/a.html'), strftime('%Y-%m-%d %H:%M:%S', datetime('now')), strftime('%Y-%m-%d %H:%M:%S', datetime('now')));
INSERT INTO posts(slug, content, created_on, updated_on)
VALUES('high-fiber-diet', readfile('blog/db/seeds/posts/b.html'), strftime('%Y-%m-%d %H:%M:%S', datetime('now')), strftime('%Y-%m-%d %H:%M:%S', datetime('now')));
INSERT INTO posts(slug, content, created_on, updated_on)
VALUES('leaf-compost', readfile('blog/db/seeds/posts/c.html'), strftime('%Y-%m-%d %H:%M:%S', datetime('now')), strftime('%Y-%m-%d %H:%M:%S', datetime('now')));
INSERT INTO posts(slug, content, created_on, updated_on)
VALUES('minima-blog-with-flask-and-html', readfile('blog/db/seeds/posts/d.html'), strftime('%Y-%m-%d %H:%M:%S', datetime('now')), strftime('%Y-%m-%d %H:%M:%S', datetime('now')));
