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

    @classmethod
    def update(cls, name, email, age, id):
        sql = "UPDATE users SET name=?, email=?, age=? WHERE id=?"
        CURSOR.execute(sql, (name, email, age, id))
        CONN.commit()

    @classmethod
    def read(cls, id):
        sql = "SELECT * FROM users WHERE id=?"
        CURSOR.execute(sql, (id,))
        return CURSOR.fetchone()
    
    @classmethod
    def delete(cls, id):
        sql = "DELETE FROM users WHERE id=?"
        CURSOR.execute(sql, (id,))
        CONN.commit()

    @classmethod 
    def get_all(cls):
        sql = "SELECT * FROM users"
        CURSOR.execute(sql)
        return CURSOR.fetchall()


print("Creating table")
User.create_table()

user1 = User("John", "john@example.com", 25)
user1.create()
print(user1.name + " created successfully")

user2 = User("Mike", "mike@example.com", 29)
user2.create()
print(user2.name + " created successfully")


User.update("Wendy", "wendy@example.com", 30, 2)
print(user1.name + " updated successfully")

# user1.delete(1)
# print(user1.name + " deleted successfully")

user2.delete(user2.id)
print(user2.name + " deleted successfully")

users = User.get_all()
for user in users:
    print(user)

print("Dropping table")
User.drop_table()
CONN.close()