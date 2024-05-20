# Sets   Dictionsaries start from line 35
#It can be initiated with curly brackets or the set() class constructor
#It is an unordered collection of unique elements

set() # => set()

# set(3, 2, 3, 'a', 'b', 'a')  # => TypeError: set expected at most 1 argument, got 6

set([3, 2, 3, 'a', 'b', 'a'])  # => {3, 'b', 'a', 2}

# pop
s = {1, 2, 3}
s.pop()  # => 1
print(s)  # => {2, 3}

# remove
s = {1, 2, 3}
s.remove(3)
print(s)  # => {1, 2}

# discard
s = {1, 2, 3}
s.discard(3)
print(s)  # => {1, 2}

# clear
s = {1, 2, 3}
s.clear()
print(s)  # => set()

# del
s = {1, 2, 3}
del s
# print(s)  # => NameError: name 's' is not defined


##########################################################3

#DICTIONARIES
# keys must be in string format
# keys must be unique
# values can be any data type
# dictionaries are enclosed in curly brackets
# dictionaries are unordered

{ "key1": "value1", "key2": "value2" }

my_dict = {"key": 1, "key": 2}
my_dict["key2"] = "value2"
print(my_dict)  # => {'key': 2, 'key2': 'value2'}

# creating dictionaries using dict() function

dict(x=1, y=2)
# => {'x': 1, 'y': 2}

# pop
my_dict = {"key": 1, "key": 2}
my_dict.pop("key")
print(my_dict)  # => {'key': 2}

# del
my_dict = {"key": 1, "key": 2}
del my_dict
# print(my_dict)  # => NameError: name 'dict' is not defined

# get
my_dict = {"key": 1, "key": 2}
my_dict.get("key")
# => 1
my_dict.get("key2")
# => None

# clear
my_dict = {"key": 1, "key": 2}
my_dict.clear()
print(my_dict)  # => {}    
