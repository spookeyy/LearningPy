# Object Relation Mapping

import sqlite3
db_connection = sqlite3.connect("database.db")
db_cursor = db_connection.cursor()

# creating owners table and cats table
db_cursor.execute("CREATE TABLE IF NOT EXISTS cats(id INTEGER PRIMARY KEY, name TEXT, breed TEXT, age INTEGER)")
db_cursor.execute("CREATE TABLE IF NOT EXISTS owners(id INTEGER PRIMARY KEY, name TEXT, age INTEGER)")

# inserting data into cats table
db_cursor.execute("INSERT INTO cats(name, breed, age) VALUES ('Ringo', 'Tabby', 4)")
db_cursor.execute("INSERT INTO cats(name, breed, age) VALUES ('Cindy', 'Maine Coon', 10)")
db_cursor.execute("INSERT INTO cats(name, breed, age) VALUES ('Dumbledore', 'Maine Coon', 11)")
db_cursor.execute("INSERT INTO cats(name, breed, age) VALUES ('Egg', 'Persian', 4)")
db_cursor.execute("INSERT INTO cats(name, breed, age) VALUES ('Misty', 'Tabby', 13)")
db_cursor.execute("INSERT INTO cats(name, breed, age) VALUES ('George Michael', 'Ragdoll', 9)")
db_cursor.execute("INSERT INTO cats(name, breed, age) VALUES ('Jackson', 'Sphynx', 7)")

# inserting data into owners table
db_cursor.execute("INSERT INTO owners(name, age) VALUES ('Bob', 31)")
db_cursor.execute("INSERT INTO owners(name, age) VALUES ('Melody', 37)")
db_cursor.execute("INSERT INTO owners(name, age) VALUES ('Sally', 42)")
db_cursor.execute("INSERT INTO owners(name, age) VALUES ('Jane', 27)")

# db_connection.commit()
# db_connection.close()


# THE LINES OF CODE ABLOVE HAVE MANY REPETITIONS. LETS MAKE THEM A FUNCTION TO MAKE OUR CODE CLEANER.
# We can write a series of methods that do the same thing.(abstract)

class Owner:
    all = []  # empty list

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.add_owner_to_all(self)
        # Owner.all.append(self)  # appending the object to the list

    @classmethod
    def add_owner_to_all(cls, owner):
        cls.all.append(owner)

    def save(self):
        sql = "INSERT INTO owners(name, age) VALUES (?, ?)"
        db_cursor.execute(sql, (self.name, self.age))
        db_connection.commit()

    @classmethod
    def get_all(cls):
        sql = "SELECT * FROM owners"
        db_cursor.execute(sql)
        return db_cursor.fetchall()


Owner("Bob", 31)
Owner("Melody", 37)

owners = Owner.get_all()
for owner in owners:
    print("Owner: ", owner)
class Cat:
    all = []  # empty list

    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age
        self.add_cat_to_all(self)
        # Cat.all.append(self)  # appending the object to the list

    @classmethod
    def add_cat_to_all(cls, cat):
        cls.all.append(cat)

    def save(self):
        sql = "INSERT INTO cats(name, breed, age) VALUES (?, ?, ?)"
        db_cursor.execute(sql, (self.name, self.breed, self.age))
        db_connection.commit()

    @classmethod
    def get_all(cls):
        sql = "SELECT * FROM cats"
        db_cursor.execute(sql)
        return db_cursor.fetchall()

    def __str__(self):
        return f"{self.name} is a {self.breed} cat and is {self.age} years old."

    @classmethod
    def create(cls, name, breed, age):
        sql = "INSERT INTO cats(name, breed, age) VALUES (?, ?, ?)"
        db_cursor.execute(sql, (name, breed, age))
        db_connection.commit()
    @classmethod
    def delete(cls, id):
        sql = "DELETE FROM cats WHERE id=?"
        db_cursor.execute(sql, (id,))
        db_connection.commit()
    
    @classmethod
    def update(cls, name, breed, age, id):
        sql = "UPDATE cats SET name=?, breed=?, age=? WHERE id=?"
        db_cursor.execute(sql, (name, breed, age, id))
        db_connection.commit()

    @classmethod
    def drop_table(cls):
        sql = "DROP TABLE IF EXISTS cats;"
        db_cursor.execute(sql)
        db_connection.commit()

Cat("Maru", "scottish fold", 3)
Cat("Sally", "scottish fold", 3)

cats = Cat.get_all()
for cat in cats:
    print(cat)

Cat.delete( 2 )
print("deleted")

# drop = Cat.drop_table()