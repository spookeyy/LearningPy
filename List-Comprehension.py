# ** - used for power
# **2 - used for square
# **3 - used for cube
# **4 - used for fourth power

squared_minus_one = list()

for n in range (1, 11):
    squared_minus_one.append((n ** 2) - 1)

print(squared_minus_one)
# => [0, 3, 8, 15, 24, 35, 48, 63, 80, 99]

# single line
squared_minus_one = [(n ** 2) - 1 for n in range(1, 11)]

print(squared_minus_one)
# => [0, 3, 8, 15, 24, 35, 48, 63, 80, 99]

# FROM TESTS IN CANVAS
def return_evens(num_list):
    #returns empty list when num_list has no evens - assert None == []
    for n in num_list:
        if n % 2 != 0:
            return []
        # returns evens from num_list - assert [] == [0, 2, 4, 6, 8]
        return [n for n in num_list if n % 2 == 0]
    return [n for n in num_list if n % 2 == 0]

def make_exclamation(sentence_list):
    #returns empty list when sentence_list is empty - assert [] == []
    if not sentence_list:
        return []
    # returns list of sentences with exclamation marks
    return [sentence + "!" for sentence in sentence_list]