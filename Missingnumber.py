a=[int(a) for a in input().split()]
n=max(a)
actual=int((n*(n+1))/2)
real=sum(a)
print (actual-real)
