import math
alpha   = []
while 1:
    n   = int(input())
    if n == 0:
        break
    s   = [float(i) for i in input().split()]
    sum = 0
    for i in s:
        sum += i
    mean    = sum/n
    alpha_2 = 0
    for i in s:
        alpha_2   += (i - mean)**2/n
    alpha.append(math.sqrt(alpha_2))
for i in alpha:
    print(i)