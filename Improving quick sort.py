import random
def calPivot(arr,left,right):
    pivot_value = arr[left]
    pivotLeft = i = left
    pivotEqual = right
    while i <= pivotEqual:
        if arr[i] < pivot_value:
            arr[i], arr[pivotLeft] = arr[pivotLeft], arr[i]
            pivotLeft += 1
            i += 1
        elif arr[i] == pivot_value:
            i += 1
        else:
            arr[i], arr[pivotEqual] = arr[pivotEqual], arr[i]
            pivotEqual -= 1
        
    return pivotLeft, pivotEqual
            
        
def quickSort(arr,l,r):
    if l >= r:
        return
    pivot = random.randint(l,r)
    arr[l], arr[pivot] = arr[pivot], arr[l]
    end,start = calPivot(arr,l,r)
    quickSort(arr,l,end-1)
    quickSort(arr,start+1,r)    


n = int(input())
arr = list(map(int,input().split(" ")))
quickSort(arr,0,n-1)
for i in arr:
    print(i,end=" ")