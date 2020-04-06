a=[int(n) for n in input().split()]
n=len(a)
l=0
r=n-1
while (l<r):
    while (a[l]!=0 and l<r):
        l+=1
    while (a[r]==0 and l<r):
        r-=1
    if (l<r):
        a[l],a[r]=a[r],a[l]
        l+=1
        r-=1
print (a)
