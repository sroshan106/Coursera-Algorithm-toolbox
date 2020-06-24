

def compute(arr,arr1,n,m):
    l = []
    for _ in range(m+1):
        l.append([0]*(n+1))

    for i in range(m+1):
        for j in range(n+1):
            if i>0 and j>0:
        
                if arr[i-1]==arr1[j-1]:
                    l[i][j]=l[i-1][j-1]+1
                else:
                    l[i][j] = max(l[i-1][j],l[i][j-1])
    return l[m][n]

n = int(input())
arr= list(map(int,input().split(" ")))
m = int(input())
arr1 = list(map(int,input().split(" ")))
print(compute(arr,arr1,m,n))