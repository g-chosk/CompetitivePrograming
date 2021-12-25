n,m,l   = [int(x) for x in input().split()]
A   = [[0 for i in range(m)] for j in range(n)]
B   = [[0 for i in range(l)] for j in range(m)]
C   = [[0 for i in range(l)] for j in range(n)]
for i in range(n):
    A[i]    = [int(x) for x in input().split()]
for i in range(m):
    B[i]    = [int(x) for x in input().split()]

for i in range(n):
    for j in range(l):
        cij = 0
        for k in range(m):
            cij += A[i][k] * B[k][j]
        print("%d"%cij,end='')
        if j != l-1:
            print("",end=" ")
    print()