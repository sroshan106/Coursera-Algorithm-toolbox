def compute(l,n):
    l.sort(reverse=True)
    print(l)


n = int(input())
l = input().split(" ")
compute(l,n)