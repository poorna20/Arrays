a=[int(a) for a in input().split()]
b=[int(b) for b in input().split()]
union=[int(i) for i in a]
inter=[]
for i in b:
    if i not in union:
        union.append(i)
    if (i in a) and (i not in inter):
        inter.append(i)
print (union,inter)
