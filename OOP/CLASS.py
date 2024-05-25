# class in python
# class is a blueprint for creating objects
# class is a user defined data type

# syntax
# class class_name:
#     def __init__(self, parameter_list):
#         self.parameter_list = parameter_list
#     def method_name(self):
#         return self.parameter_list

# example

class Animal:
    # constructor - init.
    def __init__(self, my_name, my_age):
        # attribute - instance variable
        self.name = my_name.title() # capitalize first letter
        self.my_age = my_age

    def printer(self):
        print(f"My name is {self.name} and I am {self.my_age} years old")

    def age(self): # instance method
        print("I am 10 years old")


# object is an instance of a class
cat = Animal("mitty", 10)
cat.printer()
# cat.age()

dog = Animal("huppy", 5)
dog.printer()
# dog.age()

# feature of init is that it is called every time an object is created
# inheritance is when a class inherits all the attributes and methods of another class
# method is a function that belongs to a class
# difference between class attribute and instance attribute is that (1) class attribute is shared by all the objects of that class, while instance attribute is unique to each object of that class


# INHERITANCE
# syntax
# class child_class(parent_class):
#     def __init__(self, parameter_list):
#         self.parameter_list = parameter_list
#     def method_name(self):
#         return self.parameter_list

# example

class Dog(Animal):
    def __init__(self, my_name, my_age, my_breed): 
        super().__init__(my_name, my_age) # super keyword is used to access the parent class
        self.breed = my_breed

    def printer(self): # overriding the method from parent class
        print(f"My name is {self.name} and I am {self.age} years old and I am a {self.breed}")


# Dog in dog.py prints "Name must be string between 1 and 25 characters." if empty string. - AssertionError: assert '' == 'Name must be...characters.\n'
# solution

# class Dog(Animal):
#     def __init__(self, my_name, my_age, my_breed):
#         super().__init__(my_name, my_age)
#         if my_name == "":
#             raise ValueError("Name must be string between 1 and 25 characters.")
#         self.breed = my_breed


# string to title case
# syntax
# string.title()

# example
string = "guido van rossum"
string.title()
# => "Guido Van Rossum"