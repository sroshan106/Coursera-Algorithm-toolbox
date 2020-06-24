def compute(a,b):
    m = len(a)
    n = len(b)
    arr=[]
    for _ in range(m+1):
        arr.append([0]*(n+1))

    for i in range(m+1):
        arr[i][0]=i
        for j in range(n+1):
            arr[0][j]=j
            if i>0 and j>0:
                if a[i-1]!=b[j-1]:
                    arr[i][j]= min(arr[i-1][j],arr[i][j-1],arr[i-1][j-1])+1
                else:
                    arr[i][j]=arr[i-1][j-1]
    return arr[m][n]
            
a = input()
b = input()
print(compute(a,b))