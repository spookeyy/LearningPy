[1, 3, 400, 7]
# => [1, 3, 400, 7]

#creating an empty list automatically
list()
# => []

list_abc = ['a', 'b', 'c']
list_abc[0]
# => 'a'
list_abc[1]
# => 'b'
list_abc[2]
# => 'c'

list_abc[0] = 'z' #replaces 'a' with 'z'
list_abc
# => ['z', 'b', 'c']

list_abc.append('d')
list_abc
# => ['z', 'b', 'c', 'd']


len([1, 3, 400, 7])
# => 4

sorted([5, 100, 234, 7, 2])
# => [2, 5, 7, 100, 234]

sorted([5, 100, 234, 7, 2], reverse=True)
# => [234, 100, 7, 5, 2]

sorted([5, 100, 234, 7, 2], key=lambda x: x % 10) #sorts by last digit of each number ( lambda is an anonymous function)
# => [5, 7, 2, 100, 234]

list_123 = [1, 2, 3]
list_123.append(4)

print(list_123)
# => [1, 2, 3, 4]


# Check if an item exists in a list
'z' in ['a', 'b', 'c']
# => False
'z' in ['a', 'b', 'c', 'z']
# => True