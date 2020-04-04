n=[int(n) for n in input().split()]
su=int(input())
for i in range(len(n)):
    s=set()
    nowreq=su-n[i]
    for j in range(i+1,len(n)):
        if (nowreq-n[j] in s):
            print (n[i],n[j],nowreq-n[j])
        s.add(n[j])
