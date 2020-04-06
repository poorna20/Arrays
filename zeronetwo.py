a=[int(n) for n in input().split()]
n=len(a)
one=1
zero=0
two=0
for i in a:
    if (i==0):
        zero+=1
    elif(i==1):
        one+=1
    else:
        two+=1
for i in range(zero):
    print (0,end='')
for i in range(one):
    print (1,end='')
for i in range(two):
    print (2,end='')
