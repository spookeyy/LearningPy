my_dict = {
    "a": 1,
    "b": 2,
    "c": 3}

# update an existing key-value pair:
my_dict["a"] = 10
print(my_dict)  # => {'a': 10, 'b': 2, 'c': 3}

# set a new key-value pair:
my_dict["d"] = 4
print(my_dict)  # => {'a': 10, 'b': 2, 'c': 3, 'd': 4}



# UPDATE METHOD.
# syntax
# dict.update(dict2)
# dict.update({key: value})

my_dict = {
    "a": 1,
    "b": 2,
    "c": 3}

# update multiple fields:
my_dict.update({"a": 10, "b": 20})
print(my_dict)  # => {'a': 10, 'b': 20, 'c': 3}

# add multiple fields:
my_dict.update({"d": 4, "e": 5})
print(my_dict)  # => {'a': 10, 'b': 20, 'c': 3, 'd': 4, 'e': 5}

# add and update simultaneously:
my_dict.update({"f": 6, "a": 11})
print(my_dict)  # => {'a': 11, 'b': 20, 'c': 3, 'd': 4, 'e': 5, 'f': 6}


#Iterating Over Dictionaries.

#DICT.items()

my_dict = {
    "a": 1,
    "b": 2,
    "c": 3,
    "d": 4
}

[key for key in my_dict.items()]
# => [('a', 1), ('b', 2), ('c', 3), ('d', 4)]

[key for key, value in my_dict.items()]
# => ['a', 'b', 'c', 'd']
[value for key, value in my_dict.items()]
# => [1, 2, 3, 4]