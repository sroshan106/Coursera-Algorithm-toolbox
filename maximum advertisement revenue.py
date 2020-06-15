def compute(profit,clicks):
    profit.sort(reverse=True)
    clicks.sort(reverse=True)
    summ=0
    for i in range(len(profit)):
        summ+=(profit[i]*clicks[i])
    return summ


n  = int(input())
profit = list(map(int,input().split(" ")))
clicks = list(map(int,input().split(" ")))
print(compute(profit,clicks))
