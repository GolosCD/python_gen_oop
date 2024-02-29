some_list = [1,2,3,4,]

child_list = some_list

child_list_two = some_list

print(id(some_list)) #2252869161280

print(id(child_list)) #2252869161280

print(id(child_list_two)) #2252869161280


some_list[:] = ['a','b','c']

print(id(some_list)) #2075339973888

print(some_list) # ['a', 'b', 'c']

print(child_list_two) # [1, 2, 3, 4]