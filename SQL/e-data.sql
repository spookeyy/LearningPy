CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    password TEXT NOT NULL,
    email TEXT NOT NULL
);
-- INSERT IGNORE
INSERT OR REPLACE INTO users IF NOT EXISTS (username, password, email)
VALUES ('meshack', 'password1', 'user1@example.com'),
       ('enock', 'password2', 'user2@example.com'),
       ('anthony', 'password3', 'user3@example.com');
-- DONT INSERT IF EXISTS
-- INSERT OR REPLACE INTO users (username, password, email)
-- VALUES ('meshack', 'password1', 'user1@example.com'),
--        ('enock', 'password2', 'user2@example.com'),
--        ('anthony', 'password3', 'user3@example.com');

SELECT * FROM users WHERE username LIKE '%a%';

SELECT * FROM users ORDER BY username; 

SELECT username, COUNT(*) FROM users GROUP BY username;

-- DELETE from users ranging from <id> to <id>
DELETE FROM users WHERE id BETWEEN 1 AND 3;