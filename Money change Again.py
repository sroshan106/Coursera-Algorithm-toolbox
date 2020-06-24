import sys
def compute(n):
    l=[1,3,4]
    arr =[sys.maxsize]*(n+1)
    arr[0]=0
    for k in l:
        for i in range(k,n+1):
            arr[i]=min((arr[i-k]+1),arr[i])
    return arr[n]



n = int(input())
print(compute(n))