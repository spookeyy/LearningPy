# A generator expression uses parenthesis
# It is similar to list comprehension
# But it is not a list
# It is a generator


# generator expression
one_to_three = range(1, 4)
squared_ge = (n ** 2 for n in one_to_three)

print(squared_ge)  # => <generator object <genexpr> at 0x000001>
print(next(squared_ge))  # => 1
print(next(squared_ge))  # => 4
print(next(squared_ge))  # => 9
# print(next(squared_ge))  # => StopIteration