def a():
    import math
    X,Y = [int(x) for x in input().split()]
    if X >= Y:
        print(0)
    else:
        print("%d"%(math.ceil((Y-X)/10)))

def b():
    L,R = [int(x) for x in input().split()]
    S   = input()
    for i in range(len(S)):
        if i >= L-1 and i <= R-1:
            print(S[R-(i-L)-2],end='')
        else:
            print(S[i],end='')
    print()

def c():
    N,X = [int(x) for x in input().split()]
    L   = [0 for i in range(N)]
    A   = [[0] for i in range(N)]
    for i in range(N):
        Array   = [int(x) for x in input().split()]
        L[i]    = Array[0]
        A[i]    = Array[1:]
    count   = 0
    index   = [0 for i in range(N)]
    while 1:
        product = 1
        for i in range(N):
            product *= A[i][index[i]]
        if product  == X:
            count   += 1
        index[0]    += 1
        for i in range(N-1):
            if index[i]  == L[i]:
                index[i+1]  += 1
                index[i]    = 0
        if index[N-1] == L[N-1]:
            break
    print(count)
c()