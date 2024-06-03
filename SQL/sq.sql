CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    password TEXT NOT NULL,
    email TEXT NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
)
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    password TEXT NOT NULL,
    email TEXT NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
)

INSERT INTO users (username, password, email)
VALUES ('user1', 'password1', 'JnQ0z@example.com'),
       ('user2', 'password2', 'b9gkZ@example.com'),
       ('user3', 'password3', 'Hb0T@example.com')

-- SQL SELECT
SELECT * FROM users

-- SQL LIKE (%a) finding any string that contains 'a'
SELECT * FROM users WHERE username LIKE '%a%' 

-- SQL ORDER BY
SELECT * FROM users ORDER BY username

-- SQL GROUP BY
SELECT username, COUNT(*) FROM users GROUP BY username

-- SQL JOIN
SELECT * FROM users
JOIN posts ON users.id = posts.user_id

-- SQL LIMIT    
SELECT * FROM users LIMIT 10

-- SQL UPDATE
UPDATE users SET username = 'newusername' WHERE id = 1

-- SQL DELETE
DELETE FROM users WHERE id = 1

-- SQL TRUNCATE
TRUNCATE TABLE users

-- SQL BETWEEN
SELECT * FROM posts WHERE created_at BETWEEN '2022-01-01' AND '2022-12-31'

-- SQL IN
SELECT * FROM users WHERE username IN ('user1', 'user2')

-- SQL EXISTS
SELECT * FROM users WHERE EXISTS (SELECT * FROM posts WHERE posts.user_id = users.id)

-- SQL RELATIONSHIP
SELECT * FROM users
JOIN posts ON users.id = posts.user_id
WHERE posts.user_id = 1

-- SQL RELATIONSHIP ONE TO MANY
SELECT * FROM users
JOIN posts ON users.id = posts.user_id

-- SQL RELATIONSHIP MANY TO MANY
SELECT * FROM users
JOIN posts ON users.id = posts.user_id
JOIN comments ON posts.id = comments.post_id

-- SQL RELATIONSHIP MANY TO ONE
SELECT * FROM posts
JOIN comments ON posts.id = comments.post_id

-- SQL SUBQUERY
SELECT * FROM users
WHERE id IN (SELECT user_id FROM posts)