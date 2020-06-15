def compute(n):
    i=1
    m=n
    while(n>0):
        n-=i
        i+=1
    i-=1
    if n<0:
        i-=1
    print(i)
    for k in range(1,i):
        print(k,end=" ")
        m-=k
    print(m)    
    



    
    

n = int(input())
compute(n)