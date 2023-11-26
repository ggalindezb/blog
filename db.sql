CREATE TABLE IF NOT EXISTS "posts" (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  slug TEXT NOT NULL,
  content TEXT NOT NULL,
  created_on INTEGER NOT NULL,
  updated_on INTEGER NOT NULL
);

INSERT INTO POSTS(slug, content, created_on, updated_on)
VALUES('welcome', 'A welcome post', strftime('%Y-%m-%d %H:%M:%S', datetime('now')), strftime('%Y-%m-%d %H:%M:%S', datetime('now')));

INSERT INTO POSTS(slug, content, created_on, updated_on)
VALUES('something', 'Something else blog post', strftime('%Y-%m-%d %H:%M:%S', datetime('now')), strftime('%Y-%m-%d %H:%M:%S', datetime('now')));
