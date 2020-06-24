import sys
def compute(n):
    arr =  [sys.maxsize]*(n+1)
    arr[0]=0
    for i in range(n):
        arr[i+1]=min(arr[i+1],arr[i]+1)
        if i<=n//2:
            arr[i*2]=min(arr[i*2],(arr[i]+1))
        if i<=n//3:
            arr[i*3] = min(arr[i*3],(arr[i]+1))
    
    i=n
    l=[]
    l.append(n)
    while i>0:
        if i%3==0 and arr[i]==arr[i//3]+1:
            l.append(i//3)
            i=i//3
        elif i%2==0 and arr[i]==arr[i//2]+1:
            l.append(i//2)
            i=i//2
        else:
            l.append(i-1)
            i-=1
    l.pop()
    l.reverse()
    return l
n = int(input())
l = compute(n)
print(len(l)-1)
for i in l:
    print(i,end=" ")