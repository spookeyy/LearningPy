my_list = [('John', 2), ('Steve', 1), ('Joe', 3)]

def sort_tuple(tuple_value):
    return tuple_value[1] # return the key we want to sort by

my_list.sort(key = sort_tuple)
# my_list.sort()
sorted_list = sorted(my_list)
print(my_list)