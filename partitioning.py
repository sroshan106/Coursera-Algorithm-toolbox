def partition(arr,n,subsetSum):
    table =[]
    for _ in range(n):
        table.append([0]*(subsetSum+1))
    for i in range(n):
        for j in range(subsetSum+1):
            table[i][0]=1
            if arr[i]>j and i>0:
                table[i][j]=table[i-1][j]
            elif arr[i]==j:
                table[i][j]=1
            elif i>0:
                table[i][j]=max(table[i-1][j],table[i-1][j-arr[i]])
    '''
    k=[]
    n-=1
    row=n
    col = subsetSum
    while True:
        if subsetSum==0 :
            break
        elif table[n][subsetSum]==1:
            if n==0:
                k.append(n)
                break
            elif table[n-1][subsetSum]==0:
                k.append(n)
                subsetSum-=arr[n]
            n-=1
        else:
            break
    
    for i in k:
        arr.pop(i)
    '''
    return table[n-1][subsetSum]
     

n = int(input())
arr = list(map(int,input().split(" ")))
summ=  sum(arr)
if summ%3!=0:
    print(0)
else:
    subsetSum = summ//3
    a = partition(arr,n,subsetSum)
    b = partition(arr,n,2*subsetSum)
    c = partition(arr,n,3*subsetSum)
    if a==1 and b==1 and c==1:
        print(1)
    else:
        print(0) 