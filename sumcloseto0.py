n=[int(n) for n in input().split()]
n.sort()
l=0
r=len(n)-1
misum=99999
while (l<r):
    sum=n[l]+n[r]
    if (abs(sum)<abs(misum)):
        misum=sum
        mil=l
        mir=r
    if ((sum)<0):
        l+=1
    else:
        r-=1
print (n[mil],n[mir])
