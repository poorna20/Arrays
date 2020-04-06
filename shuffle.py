import random
n=[int(n) for n in input().split()]
l=len(n)
for i in range(l-1,-1,-1):
    j=random.randint(0,i+1)
    n[i],n[j]=n[j],n[i]

print (n)
