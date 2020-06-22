def compute(arr,n):
    dict={}
    for i in arr:
        if i not in dict:
            dict[i]=1
        else:
            dict[i]+=1
    
    for i in dict.values():
        if i>n//2:
            return 1
    return 0

n = int(input())
arr = list(map(int,input().split(" ")))
print(compute(arr,n))
