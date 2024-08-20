def ArrayChallenge(num):
  list = []

  for i in str(num):
    list.append(int(i))
  
  new_list = []
  for i in list:
    new_int = num * i
    new_list.append(str(new_int))

  new_int = int("".join(new_list))

  adjacent = []
  for i in str(new_int):
    adjacent.append(i)

  final = []
  for i in range(len(adjacent)):
    adjacent[i] = int(adjacent[i])
    if adjacent[i]  == adjacent[i-1] and adjacent[i] == adjacent[i+1]:
      final.append(adjacent[i])
      
  print("final", final)
  print("new_int", new_int, "adjacent", adjacent)

  
  
  print("list", list)
  print("new_list", new_list)
  return num

ArrayChallenge(134)
# print(ArrayChallenge(input()))