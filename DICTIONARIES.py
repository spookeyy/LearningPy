key_vocab = {
    "Mapping": "a data structure in which data is stored in random order \
        and accessed using immutable keys.",
    "Arbitrary": "describes data whose value is unimportant to the data type \
        or structure in which it is contained."
}

key_vocab["Mapping"]
# "a data structure in which data is stored in random order and accessed using immutable keys."
key_vocab["Arbitrary"]
# "describes data whose value is unimportant to the data type or structure in which it is contained."

# storing different types of data
software_engineer = {
    "languages": ["JavaScript", "Python"],
    "certifications": ["Flatiron School Certificate of Completion"],
    "experience": "3 months and counting!",
}

# dictionary mapping.
size_to_ounce_map = {
    "small": 12,
    "medium": 16,
    "large": 24
    }

# wrap in a function
def pour_coffee(size):
    size_to_ounce_map = {
        "small": 12,
        "medium": 16,
        "large": 24
        }
    return size_to_ounce_map[size]

pour_coffee("medium")
# => 16
pour_coffee("small")
# => 12


# dictionary comprehension
# syntax
# {key: value for key, value in iterable}

# example
{key: value for key, value in enumerate(range(10))}
# => {0: 0, 1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9}