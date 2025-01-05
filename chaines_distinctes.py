s1 = "hello tina"
s2 = "cv?"
s3 = "hii"

commons_char = set(s1)&set(s3) 
if commons_char:
    print("pas distinctes")
else :
    print("distinctes")

#Méthode 2

print(set(s2).isdisjoint(set(s2)))
print(set(s2).isdisjoint(set(s3)))