def merge(arr, low, mid, high): 
    n1 = mid - low + 1
    n2 = high- mid 
    L = [0]*n1 
    R = [0]*n2 
    for i in range(n1): 
        L[i] = arr[low + i] 
    for j in range(n2): 
        R[j] = arr[mid + 1 + j] 
    counter=0
    i = 0      
    j = 0     
    k = low      
    while i < n1 and j < n2 : 
        if L[i] <= R[j]: 
            arr[k] = L[i] 
            i += 1
        else: 
            arr[k] = R[j] 
            print(R[j])
            j += 1
            counter+=1
            
        k += 1
    while i < n1: 
        arr[k] = L[i] 
        print(L[i])
        i += 1
        k += 1
        counter+=1
        
        
    while j < n2: 
        arr[k] = R[j] 
        j += 1
        k += 1
    return counter
    

def mergeSort(arr,low, high):
    counter=0
    if low>=high:
        return 0
    mid = (low+high)//2
    c1 = mergeSort(arr,low,mid)
    c2 = mergeSort(arr,mid+1,high)
    c3 = merge(arr,low,mid,high)
    counter = counter+c1+c3+c2
    return counter





n = int(input())
arr = list(map(int,input().split(" ")))
counter =mergeSort(arr,0,n-1)
print(counter)
print(arr)
