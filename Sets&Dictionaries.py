# Sets   Dictionaries start from line 35
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

sentence = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."
unique_consonants = {c.lower() for c in sentence if c not in "aeiou ,."}
print(unique_consonants) 
# => {'l', 'r', 'm', 's', 'd', 't', 'c', 'i', 'a', 'g', 'u', 'e', 'b', 'o', 'p', 'h'}

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


dog = "cuddly"

dict_map = {
    "hungry": "Refilling food bowl.",
    "thirsty": "Refilling water bowl.",
    "playful": "Playing tug-of-war.",
    "cuddly": "Snuggling.",
}

# Remember that a dictionary's .get() method lets us set a default value!
owner = dict_map.get(dog, "Reading newspaper.")
print(owner)  # => "Snuggling."