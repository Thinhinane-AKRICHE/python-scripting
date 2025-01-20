my_dict = {"x": "y"}
correspondance = {"y": "z"}

result ={}
for k, v in my_dict.items():
    if v in correspondance.keys():
        result[k] = correspondance[v]

print(result)