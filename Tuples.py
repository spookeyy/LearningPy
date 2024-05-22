#tuples
# Tuples are nearly identical to lists, except that they are immutable
# Tuples are created with the tuple() function
# Tuples are created with round brackets

# Tuples are immutable. once created, they cannot be changed

(1, 2, 3)
# => (1, 2, 3)
tuple([1, 2, 3])
# => (1, 2, 3)

# used in in data retrieved from a database. 
# Since you want to keep an accurate record of what is in the database while your application works with the data, a tuple will protect that information until it is no longer needed.

# when creating a single tuple,
student = ("John",) # note the comma
print(student) # print(type(student)) => <class 'tuple'>
# => ("John",)
