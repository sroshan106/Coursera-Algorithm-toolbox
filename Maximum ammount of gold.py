def compute(w,n,arr):
    l=[]
    for _ in range(n+1):
        l.append([0]*(w+1))
    for i in range(n+1):
        for  w in range(w+1):
            if i==0 or w==0:
                l[i][w]=0
            elif arr[i-1]<=w:
                l[i][w]=max(arr[i-1]+ l[i-1][w-arr[i-1]],l[i-1][w])
            else:
                l[i][w]=l[i-1][w]
    return l[n][w]

l = list(map(int,input().split(" ")))
w = l[0]
n = l[1]
arr = list(map(int,input().split(" ")))
print(compute(w,n,arr))