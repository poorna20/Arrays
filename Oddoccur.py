a=[int(a) for a in input().split()]
d=dict()
for i in a:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
for i in d:
    if (d[i]%2!=0):
        print (i)
