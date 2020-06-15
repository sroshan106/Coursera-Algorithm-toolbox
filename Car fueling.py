def compute(d,m,l):
    
    n = len(l)-1
    i=0
    counter=0
    while(i<n):
        temp = l[i]
        var = m
        while var>0 and i<n:
            diff =  l[i+1]-l[i]
            var-=diff
            if var>=0:
                
                i+=1
        if temp == l[i]:
            return -1
        if d==l[i]:
            return counter
        counter+=1
        
    return counter

d = int(input())
m = int(input())
n = int(input())
l = list(map(int,input().split(" ")))
l.insert(0,0)
l.append(d)
print(compute(d,m,l))
