my_dict = {"pi": 3.14, "mot": "mot", "nombre": 42, "list": [1,2,3]}
my_dict["nombre"] = "hello"

mot = input()
if mot in my_dict:
    print(mot, "vaut", my_dict[mot], "dans my_dict")
else:
    print(mot, "n'est pas une cle dans my_dict")