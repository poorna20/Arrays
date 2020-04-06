a=[int(n) for n in input().split()]
n=len(a)
l=0
r=n-1
while (l<r):
    while (a[l]<0 and l<r):
        l+=1
    while (a[r]>0 and l<r):
        r-=1
    if (l<r):
        a[l],a[r]=a[r],a[l]
        l+=1
        r-=1
pos=0
neg=1
for i in range(n):
    if (a[i]<0):
        pos+=1
while (pos<n and neg<n):
    a[neg],a[pos]=a[pos],a[neg]
    pos+=1
    neg+=2
print (a)
