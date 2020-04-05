n=[int(n) for n in input().split()]
n.sort()
mi=99999
for i in range(1,len(n)):
    mi=min(n[i]-n[i-1],mi)
print (mi)
    
