my_list = [1,2,3,4,5]

sub1 = my_list [:3]
sub2 = my_list [1:3]
sub3 = my_list [-3:]
sub4 = my_list [::2]
sub5 = my_list [1::2]
sub6 = my_list [::-1]

print(sub1, sub2, sub3, sub4, sub5, sub6)