def gennextpalin(num,n):
    mid=int(n/2)
    i=mid-1
    j=mid+1 if (n%2) else mid
    leftsmaller=False
    while (i>=0 and num[i]==num[j]):
        i-=1
        j+=1
    if (i<0 or num[i]<num[j]):
        leftsmaller=True
    while (i>=0):
        num[j]=num[i]
        i-=1
        j+=1
    if (leftsmaller):
        carry=1
        i=mid-1
        if (n%2==1):
            num[mid]+=carry
            carry=int(num[mid]/10)
            num[mid]%=10
            j=mid+1
        else:
            j=mid
        while (i>=0):
            num[i]+=carry
            carry=int(num[i]/10)
            num[i]%=10
            num[j]=num[i]
            j+=1
            i-=1

    for i in num:
        print (i,end='')
    
def isall9(num,n):
    for i in num:
        if i!=9:
            return False
    return True
def all9(num,n):
    print ("1")
    for i in range(n-1):
        print ("0")
    print ("1")

def genpalin(num,n):
    if (isall9(num,n)):
        all9(num,n)
    else:
        gennextpalin(num,n)

num=[int (num) for num in input().split()]
n=len(num)
genpalin(num,n)
        
    
