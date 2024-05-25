class Dog:
    def __init__(self, name, breed="Mutt"):
        # takes a name as an argument and saves it to self.name
        self.name = name
        self.breed = breed

    def bark(self):
        print("Woof!")


class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello, my name is {self.name}")