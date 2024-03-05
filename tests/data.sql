-- Users
INSERT INTO users(key, created_on, updated_on)
VALUES('00000000-0000-0000-0000-000000000000',
  strftime('%Y-%m-%d %H:%M:%S', datetime('now')),
  strftime('%Y-%m-%d %H:%M:%S', datetime('now')));

-- Posts
INSERT INTO posts(slug, brief, content, created_on, updated_on)
VALUES('post-1',
  readfile('Post 1 slug'),
  readfile('Post 1 content'),
  strftime('%Y-%m-%d %H:%M:%S', datetime('now')),
  strftime('%Y-%m-%d %H:%M:%S', datetime('now')));
INSERT INTO posts(slug, brief, content, created_on, updated_on)
VALUES('post-2',
  readfile('Post 2 slug'),
  readfile('Post 2 content'),
  strftime('%Y-%m-%d %H:%M:%S', datetime('now')),
  strftime('%Y-%m-%d %H:%M:%S', datetime('now')));
INSERT INTO posts(slug, brief, content, created_on, updated_on)
VALUES('post-3',
  readfile('Post 3 slug'),
  readfile('Post 3 content'),
  strftime('%Y-%m-%d %H:%M:%S', datetime('now')),
  strftime('%Y-%m-%d %H:%M:%S', datetime('now')));
INSERT INTO posts(slug, brief, content, created_on, updated_on)
VALUES('post-4',
  readfile('Post 4 slug'),
  readfile('Post 4 content'),
  strftime('%Y-%m-%d %H:%M:%S', datetime('now')),
  strftime('%Y-%m-%d %H:%M:%S', datetime('now')));
