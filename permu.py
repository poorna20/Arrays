def nextpermu(num,n):
    for i in range(n-1,0,-1):
        if (num[i]>num[i-1]):
            break
    if (i==1 and num[i]<=num[i-1]):
        print (-1)
        return
    x=num[i-1]
    smallest=i
    for j in range(i+1,n):
        if (num[j]>x and num[j]<num[smallest]):
            smallest=j
    num[i-1],num[smallest]=num[smallest],num[i-1]
    new=sorted(num[i:])
    for j in range(i):
        print (num[j],end='')
    for i in new:
        print (i,end='')

num=[int(num) for num in input().split()]
n=len(num)
nextpermu(num,n)
