n=[int(n) for n in input().split()]
diff=0
for i in range(1,len(n)):
    diff=max(n[i]-min(n[:i]),diff)
print (diff)

    
