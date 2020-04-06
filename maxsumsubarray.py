n=[int(n) for n in input().split()]
currmax=0
maxsofar=0
for i in range(len(n)):
    currmax=max(n[i],currmax+n[i])
    maxsofar=max(maxsofar,currmax)
print (maxsofar)
