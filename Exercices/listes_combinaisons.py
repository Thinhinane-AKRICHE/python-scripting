my_list = [0,1,2,3,4,5,6]

l1 = my_list [0:len(my_list)]+ my_list[::-1]
#l1 = my_list + my_list[::-1]
#l1 = my_list [::]+ my_list[::-1]

#l2 = my_list[:3]+my_list[:3]+my_list[:3] 
l2 = my_list[:3] * 3

l3 = my_list[::3]
print(l3)