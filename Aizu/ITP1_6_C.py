n   = int(input())
count   = [[[0 for i in range(10)] for j in range(3)] for k in range(4)]
for i in range(n):
    b,f,r,v = map(int,input().split())
    count[b-1][f-1][r-1]  += v
b = 1
while b <=4:
    for f in range(1,3+1):
        for r in range(1,10+1):
            print(" %d"%count[b-1][f-1][r-1],end='')
        print("")
    if b <= 3:
        print("#"*20)
    b+=1
