def compute(maxx,value,weight):
    temp = []
    length = len(weight)
    for i in range(length):
        temp.append(value[i]/weight[i])
    weight= [x for _,x in sorted(zip(temp,weight),reverse=True)]
    temp.sort(reverse=True)
    summ=0
    for i in range(length):
        if maxx==0:
            return summ
        elif weight[i]<=maxx:
            maxx-=weight[i]
            summ+=weight[i]*temp[i]
        else:
            summ+=maxx*temp[i]
            maxx=0
    return summ


l = list(map(int,input().split(" ")))
n=l[0]
maxx=l[1]
weight=[]
value =[]
for i in range(n):
    temp = list(map(int,input().split(" ")))
    value.append(temp[0])
    weight.append(temp[1])
k=compute(maxx,value,weight)
k = round(k,4)
print("{:.4f}".format(k))