Array   = []
while 1:
    n,x = map(int,input().split())
    if (n,x) == (0,0):
        break
    else:
        Array.append([n,x])

for [n,x] in Array:
    cnt = 0
    for i in range(1,n-2+1,1):
        for j in range(i+1,n-1+1,1):
            for k in range(j+1,n+1,1):
                if i+j+k == x:
                    cnt += 1
    print(cnt)