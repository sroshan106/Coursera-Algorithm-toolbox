def binarySearch(arr,n,i):
    low = 0
    high = n
    while(low<high):
        mid = (low+high )//2
        if i==arr[mid]:
            return mid
        elif i>arr[mid]:
            low = mid+1
        else:
            high=mid
    return -1

def compute(arr,n,l):
    for i in l:
        print(binarySearch(arr,n,i),end = " ")


arr = list(map(int,input().split(" ")))
n =  arr.pop(0)
l = list(map(int,input().split(" ")))
k = l.pop(0)
compute(arr,n,l)

