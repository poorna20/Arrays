n=[int(n) for n in input().split()]
smaller=[0]*len(n)
smaller[0]=-1
larger=[0]*len(n)
larger[len(n)-1]=-1
min=0
for i in range(1,len(n)):
    if (n[min]>=n[i]):
        min=i
        smaller[i]=-1
    else:
        smaller[i]=min
max=len(n)-1
for j in range(len(n)-2,-1,-1):
    if (n[max]<=n[j]):
        max=j
        larger[j]=-1
    else:
        larger[j]=max

for i in range (len(n)):
    if (smaller[i]!=-1 and larger[i]!=-1):
        print (n[smaller[i]],n[i],n[larger[i]])
        
