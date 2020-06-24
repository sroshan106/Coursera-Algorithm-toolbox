
def compute(arr,arr1,arr2,n,m,o):
    l=[]
    for _ in range(m+1):
        k=[]
        for _ in range(n+1):
            k.append([0]*(o+1))
        l.append(k)
    
    for i in range(m+1):
        for j in range(n+1):
            for k in range(o+1):
                if i>0 and j>0 and o>0:
                    if arr[i-1]==arr1[j-1] and arr1[j-1]==arr2[k-1]:
                        l[i][j][k]=(l[i-1][j-1][k-1])+1
                    else:
                        l[i][j][k] = max(l[i-1][j][k],l[i][j-1][k],l[i][j][k-1])
    return l[m][n][o]

n = int(input())
arr= list(map(int,input().split(" ")))
m = int(input())
arr1 = list(map(int,input().split(" ")))
o = int(input())
arr2 = list(map(int,input().split(" ")))
print(compute(arr,arr1,arr2,m,n,o))