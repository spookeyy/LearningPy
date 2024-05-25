def divide(num1, num2):
    try:
        quotient = num1 / num2
        print(quotient)
    except ZeroDivisionError:
        print("Error: num2 cannot be equal to 0")
    except TypeError:
        print("Error: input must be of type int or float")
    finally: # this will be executed no matter what
        print("Isn't division fun?")

divide(10, 0)
# => Error: You can't divide by zero!

divide(10, 5)
# => 2

# try-except is a good way to handle errors.

# Use of the finally keyword at the end of a try/except statement 
# allows us to perform actions that we want to occur regardless of 
# whether or not an exception has been thrown.