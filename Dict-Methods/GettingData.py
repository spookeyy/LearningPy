# GETTING DATA

# dict.get()
# get(key, default=None)

# example
my_dict = {
    "a": 1,
    "b": 2,
    "c": 3
}

my_dict.get("a")
# => 1
my_dict.get("d")
# => None
my_dict.get("d", "Not found")
# => "Not found"

def pour_coffee(size):
    size_to_ounce_map = {
        "small": 12,
        "medium": 16,
        "large": 24
        }
    return size_to_ounce_map.get(size, "Enter Valid cup size")
# return size_to_ounce_map.get(size, 0)
pour_coffee("medium")
# => 16
pour_coffee("small")
# => 12
pour_coffee("jumbo")
# => 0 - 0 is the default value. if no value is passed, by default, None is returned
# => Enter Valid cup size

