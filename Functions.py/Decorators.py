# for decorators:
# https://realpython.com/primer-on-python-decorators/

# Decorators are functions that take other functions as arguments
# and return a new function.

# 1. Takes a function as an argument
# 2. Has an inner function defined inside of it
# 3. Returns the inner function


# syntax
# @decorator
# def function(parameter_list):
#     statement(s)
#     return value


# example
def decorator(func):
    def wrapper():
        print("I am the output that lets you know the function is about to be called.")
        func()
        print("I am the output that lets you know the function has been called.")
    return wrapper

def get_called():
    print("I am the function that gets called.")

get_called = decorator(get_called)
get_called()
# I am the output that lets you know the function is about to be called.
# I am the function and I am being called.
# I am the output that lets you know the function has been called.

#  "pie syntax"
@decorator
def get_Called():
    print("I am the function and I am about to be called.")

get_Called()
# I am the output that lets you know the function is about to be called.
# I am the function and I am being called.
# I am the output that lets you know the function has been called.

