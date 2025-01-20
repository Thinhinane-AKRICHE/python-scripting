dic = { 'a':1, 'b':1, 'c':2, 'd':3, 'e':2}
inv_deco = {i : [] for i in dic.values()}


for k,v in dic.items():
    inv_deco[v].append(k)
print(inv_deco)   