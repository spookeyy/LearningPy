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

