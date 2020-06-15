def IsGreaterOrEqual(digit, max_digit):
    return int(str(digit)+str(max_digit))>=int(str(max_digit)+str(digit))

def compute(l):
    answer = []
    
    while l!=[]:
        max_digit = 0
        for digit in l:
            if IsGreaterOrEqual(digit, max_digit):
                max_digit = digit
        answer.append(max_digit)
        l.remove(max_digit)

    return answer




n = int(input())
l = input().split(" ")
k = compute(l)
string=''
for i in k:
    string+=str(i)
print(string)