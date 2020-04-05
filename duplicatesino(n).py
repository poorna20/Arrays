n=[int(n) for n in input().split()]
for i in range(len(n)):
    if (n[abs(n[i])])>=0:
        n[abs(n[i])]=-n[abs(n[i])]
    else:
        print (abs(n[i]))
