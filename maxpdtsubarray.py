n=[int(n) for n in input().split()]
maxendinghere=1
minendinghere=1
maxsofar=1
flag=0
for i in range(len(n)):
    if n[i]>0:
        maxendinghere=maxendinghere*n[i]
        minendinghere=min(minendinghere*n[i],1)
        flag=1
    elif n[i]==0:
        maxendinghere=0
        minendinghere=0
    else:
        temp=maxendinghere
        maxendinghere=max(minendinghere*n[i],1)
        minendinghere=temp*n[i]
    if (maxsofar<maxendinghere):
        maxsofar=maxendinghere
if maxsofar==1 or flag==0:
    print (0)
else:
    print (maxsofar)
