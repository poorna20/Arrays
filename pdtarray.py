n=[int(n) for n in input().split()]
left=[0]*len(n)
right=[0]*len(n)
prod=[0]*len(n)
left[0]=1
right[len(n)-1]=1
for i in range(1,len(n)):
    left[i]=n[i-1]*left[i-1]
for i in range(len(n)-2,-1,-1):
    right[i]=right[i+1]*n[i+1]
for i in range(len(n)):
    prod[i]=left[i]*right[i]
print (prod)
