# for loop
students = ['jack', 'jill', 'john', 'jane']

print(len(students))


# for loop
for x in students:
    print(x)

newArray = []
# for loop with index
for i in range(len(students)):
    newArray.append(students[i]+ " " +str(i)) #appends to new array
    print(students[i], "is at index ", i)

print(newArray)

# check if item is in liat

if "jack" in students:
    print("jack is in the list")
else:
    print("jack is not in the list")