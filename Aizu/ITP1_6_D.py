n,m = [int(x) for x in input().split()]
A   = [[0 for i in range(m)]for k in range(n)]
b   = [0 for i in range(m)]
for i in range(n):
    A[i]  = [int(x) for x in input().split()]
for i in range(m):
    b[i]    = int(input())

for i in range(n):
    ci  = 0
    for j in range(m):
        ci  += A[i][j]*b[j]
    print(ci)