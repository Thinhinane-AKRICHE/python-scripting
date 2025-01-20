my_list = [1,2,3,4,5]
my_list = [0] + my_list + [10]
my_list.insert(0,-1)
my_list.insert(len(my_list),11)
my_list.append(12)
print(my_list)