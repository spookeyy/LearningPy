# Relationships in python.
# 1. One to one
# 2. One to many
# 3. Many to one
# 4. Many to many

# 1. One to one

# example
# one person has one phone number
# one phone number belongs to one person

# BASIC SYNTAX

class Person:
    def __init__(self, name):
        self.name = name
    def greet(self):
        print(f"Hello, my name is {self.name}")

class Phone:
    def __init__(self, number):
        self.number = number
    def call(self):
        print(f"Calling {self.number}...")


# EXAMPLE

person = Person("John")
person.greet()
phone = Phone("123-456-7890")
person.phone = phone
person.phone.call()


# 2. One to many
    # example
    # A library has many books
    # one book belongs to one library

class Book:
    def __init__(self, title):
        self.title = title

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

Book1 = Book("The Great Gatsby")
Book2 = Book("To Kill a Mockingbird")
Library1 = Library()
Library1.add_book(Book1)
Library1.add_book(Book2)
Library1.books



# 3. Many to one

class Course:
    def __init__(self, name):
        self.name = name
        self.students = []
    def add_student(self, student):
        self.students.append(student)

class Student:
    def __init__(self, name):
        self.name = name
        self.courses = []

    def add_course(self, course):
        self.courses.append(course)

course1 = Course("Computer Science")
course2 = Course("Software Engineering")
course3 = Course("Data Science")

student1 = Student("John")
student2 = Student("Jane")

course1.add_student(student1)
course2.add_student(student1)
course3.add_student(student1)

student1.add_course(course1)
student1.add_course(course2)
student1.add_course(course3)

# 4. Many to many

# example
# A teacher has many students
# A student has many teachers
# A student can be in multiple teachers
# A teacher can be in multiple students

class Teacher:
    def __init__(self, name):
        self.name = name
        self.students = []
    def add_student(self, student):
        self.students.append(student)

class Student:
    def __init__(self, name):
        self.name = name
        self.teachers = []
    def add_teacher(self, teacher):
        self.teachers.append(teacher)

student_1 = Student("John")
student_2 = Student("Jane")
teacher_1 = Teacher("Kelvin")
teacher_2 = Teacher("Faith")

student_1.add_teacher(teacher_1)
student_1.add_teacher(teacher_2)
student_2.add_teacher(teacher_1)
student_2.add_teacher(teacher_2)