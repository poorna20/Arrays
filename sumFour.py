def four(n,su):
    d=dict()
    for i in range(len(n)):
        for j in range(i+1,len(n)):
            d[n[i]+n[j]]=[n[i],n[j]]      
    for i in range(len(n)):
        for j in range(i+1,len(n)):
            sumi=n[i]+n[j]
            if (su-sumi) in d:
                if (n[i]!=d[su-sumi][0] and n[i]!=d[su-sumi][1] and n[j]!=d[su-sumi][0] and n[j]!=d[su-sumi][1]):
                    print (n[i],n[j],d[su-sumi][0],d[su-sumi][1])
                    return 




n=[int(n) for n in input().split()]
su=int(input())
four(n,su)

            
