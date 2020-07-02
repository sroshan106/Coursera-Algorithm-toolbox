import math
def calc(a, b, op):

    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    else:
        return a * b
def minAndMax(maxx, minn, i, j):
    min_value = math.inf
    max_value = -math.inf
    global op
    for k in range(i, j):
        a = calc(maxx[i][k], maxx[k+1][j], op[k])
        b = calc(maxx[i][k], minn[k+1][j], op[k])
        c = calc(minn[i][k], maxx[k+1][j], op[k])
        d = calc(minn[i][k], minn[k+1][j], op[k])
        min_value = min(min_value, a, b, c, d)
        max_value = max(max_value, a, b, c, d)
    return min_value, max_value

def compute(d,op):
    n = len(d)
    minn = []
    maxx = []
    for _ in range(n):
        minn.append([0]*n)
    for _ in range(n):
        maxx.append([0]*n)
    for i in range(n):
        minn[i][i] = d[i]
        maxx[i][i] = d[i]
        
    for s in range(1, n):
        for i in range(0, n-s):
            j = i + s
            minn[i][j], maxx[i][j] = minAndMax(maxx, minn, i, j)

    return maxx[0][n-1]


s=input()
d=[]
op=[]
for i in s:
    if i in ['+', '-', '*']:
        op.append(i)
    else:
        d.append(int(i))
print(compute(d,op))