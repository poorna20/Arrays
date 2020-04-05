n=[int(n) for n in input().split()]
pos=[]
for i in range(len(n)):
    if (n[i]>=0):
        pos.append(n[i])
print ((min(pos)-1) if (min(pos)>0) else (max(pos)+1))
