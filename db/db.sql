CREATE TABLE IF NOT EXISTS "posts" (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  slug TEXT NOT NULL,
  content TEXT NOT NULL,
  created_on INTEGER NOT NULL,
  updated_on INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS "users" (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  key BLOB NOT NULL,
  created_on INTEGER NOT NULL,
  updated_on INTEGER NOT NULL
);

INSERT INTO posts(slug, content, created_on, updated_on)
VALUES('welcome', 'A welcome post', strftime('%Y-%m-%d %H:%M:%S', datetime('now')), strftime('%Y-%m-%d %H:%M:%S', datetime('now')));

INSERT INTO posts(slug, content, created_on, updated_on)
VALUES('something', 'Something else blog post', strftime('%Y-%m-%d %H:%M:%S', datetime('now')), strftime('%Y-%m-%d %H:%M:%S', datetime('now')));

INSERT INTO users(key, created_on, updated_on)
VALUES('2a1e0fc0-7bab-4aa0-9e2f-23d7ddd81241', strftime('%Y-%m-%d %H:%M:%S', datetime('now')), strftime('%Y-%m-%d %H:%M:%S', datetime('now')));
