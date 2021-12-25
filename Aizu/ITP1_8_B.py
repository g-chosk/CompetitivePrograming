X   = []
while 1:
    x   = int(input())
    if x == 0:
        break
    else:
        X.append(x)
for i in X:
    cnt = 0
    for j in str(i):
        cnt += int(j)
    print(cnt)