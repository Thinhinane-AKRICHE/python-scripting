s1 ="HELLO WORLD"
s2 ="HELLO KATY"

x1 = s1.lower().split()
x2 = s2.lower().split()

common = set(x1) & set(x2)

s1 = " ".join(m.upper() if m in common else m.lower() for m in x1)
s2 = " ".join(m.upper() if m in common else m.lower() for m in x2)

print(s1,'\n', s2)