l = [4,5,9,78,20,5]
s = {1,2,3}

l.append('y')
s.add(5)

print(l, '\n', s)
#l = [x for x in l if x != 5]
if 5 in l :
    l.remove(5)
s = {x for x in s if x != 5}
print(l, '\n', s)