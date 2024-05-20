# Python
dog_name = "lucy"
print(f"Say hello to my dog {dog_name}")
# => Say hello to my dog Lucy

#advanced formatting
price_1 = 10
price_2 = 20.5
print(f"Price 1: {price_1},\nprice 2: {price_2}")
# => Price 1: 10, price 2: 20

print(f"item 1 costs ${price_1:.2f}") # => item 1 costs $10.00(2 digits after decimal)
print(f"item 2 cost ${price_2:0.2f}") # => item 2 cost $20.50(2 digits after decimal)

# .capitalize()
print(f"hello {dog_name.capitalize()}")
# => hello Lucy

# .upper()
print(f"hello {dog_name.upper()}")
# => hello LUCY

# .lower()
print(f"hello {dog_name.lower()}")
# => hello lucy

type("hello")
# => <class 'str'>

# Using the dir() function on any Python object will display a list of all the methods that object responds to 
dir("hello")
# => ['__add__', '__class__', '__contains__', ...

