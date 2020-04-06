n=[int(n) for n in input().split()]
l=len(n)
d=dict()
for i in n:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
for i in sorted(d,key=d.get,reverse=True):
    for j in range(d[i]):
        print (i,end='')
    
