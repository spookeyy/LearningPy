import sqlite3
CONN = sqlite3.connect('users.db')
CURSOR = CONN.cursor()

class User:
    def __init__(self, name, email, age):
        self.id = None
        self.name = name
        self.email = email
        self.age = age

    # CRUD Operations
    @classmethod
    def create_table(cls):
        sql = """CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name VARCHAR(50) NOT NULL,
            email VARCHAR(50) UNIQUE NOT NULL,
            age INTEGER NOT NULL
        );"""
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql = "DROP TABLE IF EXISTS users;"
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        sql = """INSERT INTO users (name, email, age) VALUES (?, ?, ?)"""
        CURSOR.execute(sql, (self.name, self.email, self.age))
        CONN.commit()

    def create(self):
        sql = """INSERT INTO users (name, email, age) VALUES (?, ?, ?)"""
        CURSOR.execute(sql, (self.name, self.email, self.age))
        CONN.commit()

    def update(self, name):
        sql = "UPDATE users SET name=?, email=?, age=? WHERE id=?"
        CURSOR.execute(sql, (self.name, self.email, self.age, name))
        CONN.commit()

print("Creating table")
User.create_table()

user1 = User("John", "john@example.com", 25)
user1.create()
print(user1.name + " created successfully")

user2 = User("Mike", "mike@example.com", 29)
user2.create()
print(user2.name + " created successfully")

user1.name = "Wendy"
user1.update(user1.name)
print(user1.name + " updated successfully")

CONN.close()