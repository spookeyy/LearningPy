# While loops 
x = 0

while x < 10:
    print("so many loops")
    x = x + 1
    print(x)

# JS
# let i = 0;
# while (i < 5) {
#   console.log("Looping!");
#   i++;
# }

# Python
i = 0
while i < 5:
    print("Looping!")
    i = i + 1

# For loops
for i in range(5):
    print("Looping!")
    print(f"i is {i}")


# JS
# for (let i = 0; i < 5; i++) {
#   console.log("Looping!");
#   console.log("i is " + i);
# }
player_heights = [0.008, 0.008, 0.008, 0.009, 0.008, 0.01, 0.009, 0.009, 0.01, 0.008, 0.009, 0.009, 0.008, 0.008, 0.008, 0.009, 0.008, 0.009, 0.01, 0.01]

inch_heights = list()
for height in player_heights:
    inch_height = height * 7920
    inch_heights.append(inch_height)


# simple version (comprehension)
inch_heights = [height * 7920 for height in player_heights]
print(inch_heights)


# for loop with index
for i in range(len(inch_heights)):
    print(inch_heights[i], "is at index ", i)

# check if item is in list or not
for height in inch_heights:
    if height == 7920:
        print("Found")
        break
else:
    print("Not Found")

#FROM CLASS TEST CANVAS CONTENT.
def happy_new_year():
    # code goes here!
    x = 10
    while x > 0:
        print(x)
        x -= 1
    print("Happy New Year!")

def square_integers(int_list):
    # code goes here!
    new_list = [integer ** 2 for integer in int_list]
    return new_list

def fizzbuzz():
    # code goes here!
    for num in range(1, 101):
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print(num)
