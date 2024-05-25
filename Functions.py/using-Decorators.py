# when to use decorators
# primary function of decorators is reducing the amount of code that you need to write.

def sweep_floors(time):
    if 1100 < time < 2100:
        print("Sweeping the floors...")
    else:
        print("I'm off duty!")

def wash_dishes(time):
    if 1100 < time < 2100:
        print("Washing the dishes...")
    else:
        print("I'm off duty!")

def chop_vegetables(time):
    if 1100 < time < 2100:
        print("Chopping the vegetables...")
    else:
        print("I'm off duty!")

# pattern from above code: 
# employees only work from 11 to 9. Including the code in every
# single function to check if anyone is working is not ideal.
# this is where decorators come in.


# decorators are functions that take other functions as arguments
# and return a new function.

# lets refactor our code above with a decorator.

def check_working_hours(func):
    def wrapper(time):
        if 1100 < time < 2100:
            func(time)
        else:
            print("I'm off duty!")
    return wrapper

@check_working_hours
def sweep_floors(time):
    print("Sweeping the floors...")

@check_working_hours
def wash_dishes(time):
    print("Washing the dishes...")

@check_working_hours
def chop_vegetables(time):
    print("Chopping the vegetables...")

sweep_floors(800) # => I'm off duty!
wash_dishes(1800) # => Washing the dishes...
chop_vegetables(1200) # => Chopping the vegetables...