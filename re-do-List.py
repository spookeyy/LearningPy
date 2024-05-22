students = ["Jack", "John", "wendy", "regina", "alex"]

# for loop
for x in students:
    print(x)

# for loop with index.
for i in range (len(students)):
    print(students[i] , "is at index", i)

check = "meshack" in students # True or False
print(check)

if "meshack" in students:
    print("meshack is in the list")
else:
    print("meshack is not in the list")

students.append("meshack")
print(students)

# list methods in python

# sort
students.sort(reverse=True)
print(students)

# reverse
students.reverse()
print(students)

# copy
students2 = students.copy()
print(students2)

# list comprehension
students3 = [x.upper() for x in students]
print(students3)

# even_numbers_up_to_100 = range(0, 101, 2)
print(range(0, 101, 2)) # => range(0, 101, 2)

# A simple pattern of numbers
# for x in range(0, 101, 2):
#     print(x)


# s * n returns a single sequence of s repeated n times.
s = "hello"
new_s = s * 5 # => "hellohellohellohellohello"

# s = [1, 2, 3, 4, 5, 4, 7, 4, 4, 10]
# s * 5 #
print(new_s)
# s = [1, 2, 3, 4, 5, 4, 7, 4, 4, 10]

students = ["jackie", "jil", "john", "janie", "jilly"]
print(students[0:3]) # => ['jack', 'jill', 'john']

# s[i:j:k] returns a slice of s from i to j with steps of k in between.
print(students[0:3:2])
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
minimum_function = min(numbers) # => 'jackie' (based on index of item)
max_function = max(numbers) # => 'jilly'

print(f"minimum {minimum_function}\nmaximum {max_function}")

numbers.count(9)
# => 1

