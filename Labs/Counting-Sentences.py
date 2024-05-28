dir(str)
# => ['__add__', '__class__', '__contains__', '__delattr__', 
# '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', 
# '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', 
# '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', 
# '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__',
# '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith',
# 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal',
# 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 
# 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 
# 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 
# 'translate', 'upper', 'zfill']


import re
class MyString:
  def __init__(self, value=""):
    self.value = value

  # is_sentence() method
  def is_sentence(self):
    if self.value.endswith("."):
      return True
    else:
      return False
    
  # is_question() method
  def is_question(self):
    if self.value.endswith("?"):
      return True
    else:
      return False
    
  # is_exclamation() method
  def is_exclamation(self):
    if self.value.endswith("!"):
      return True
    else:
      return False
    
  # count_sentences() method
  # call a count_sentences() method on a MyString instance, and get back a, well, count of sentences in its value
  # if the value is not a sentence, return 0

  def count_sentences(self):
        if not isinstance(self.value, str):
            print("The value must be a string.\n")
            return 0

        # Split the string into sentences using regex
        sentences = re.split(r'[.!?]+', self.value)

        # Filter out empty strings
        sentences = [s.strip() for s in sentences if s.strip()]

        # Count the number of non-empty sentences
        sentence_count = len(sentences)

        return sentence_count

string = MyString()
string.value = "This is a string! It has three sentences. Right?!"
print(string.count_sentences())  # => 3
