n=[int(n) for n in input().split()]
presum=set()
presum.add(n[0])
flag=False
for i in range(1,len(n)):
    n[i]+=n[i-1]
    presum.add(n[i])
print (presum)
if (len(presum)<len(n)) or (0 in presum):
        print ("Yes")
else:
    print ('NO')
