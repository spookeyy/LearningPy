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
    def __init__(self, my_name, my_age):
        # attribute - instance variable
        self.name = my_name
        self.age = my_age

    def printer(self):
        print(f"My name is {self.name} and I am {self.age} years old")

    def age(self):
        print("I am 10 years old")


# object is an instance of a class
cat = Animal("kitty", 10)
cat.printer()
# cat.age()

dog = Animal("puppy", 5)
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

    def printer(self):
        print(f"My name is {self.name} and I am {self.age} years old and I am a {self.breed}")