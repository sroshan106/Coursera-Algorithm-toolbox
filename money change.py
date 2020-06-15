def compute(m):
    counter=0
    if m>=10:
        counter += m//10
        m=m%10
    if m>=5:
        counter +=m//5
        m=m%5
    if m>=1:
        counter+=m
        m=m%1
    return counter

m = int(input())
print(compute(m))