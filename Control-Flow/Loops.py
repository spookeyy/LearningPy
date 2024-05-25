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