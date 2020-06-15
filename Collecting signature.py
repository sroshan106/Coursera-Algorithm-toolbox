import operator
def compute(l):
    l = sorted(l,key = operator.itemgetter(1))
    k=[]
    temp=-1
    i=0
    length = len(l)
    while(i<length):
        start = l[i][0]
        end = l[i][1]
        temp = end
        k.append(temp)
        while temp>=start and temp<=end and i<length:
            i+=1
            try:
                start = l[i][0]
                end = l[i][1]
            except:
                pass
        
    print(len(k))
    for i in k:
        print(i,end =" ")

n = int(input())
l=[]
for i in range(n):
    l.append(list(map(int,input().split(" "))))
compute(l)