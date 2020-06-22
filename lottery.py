def compute(seg,points):
    l =[0]*(2*10**8)
    for i in seg:
        a = i[0]
        b = i[1]
        for k in range(a,b+1):
            l[k+10**8]+=1
    for i in points:
        print(l[i+10**8],end =" ")



l = list(map(int,input().split(" ")))
s = l[0]
p = l[1]
seg=[]
for i in range(s):
    seg.append(list(map(int,input().split(" "))))

points = list(map(int,input().split(" ")))
compute(seg,points)