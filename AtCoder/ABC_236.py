def A():
    S = str(input())
    a,b = [int(x) for x in input().split()]
    for i in range(len(S)):
        if i == a-1:
            print(S[b-1],end='')
        elif i == b-1:
            print(S[a-1],end='')
        else:
            print(S[i],end='')

def B():
    N   = int(input())
    A   = [int(a) for a in input().split()]
    List    = [0] * N
    for a in A:
        List[a-1] += 1
    print(List.index(3)+1)

def C():
    N,M = [int(x) for x in input().split()]
    S   = [str(s) for s in input().split()]
    T   = [str(t) for t in input().split()]
    rest_n_st   = 0
    stop_flag   = [0]*N
    for m in range(M):
        for n in range(rest_n_st,N,1):
            if T[m] == S[n]:
                stop_flag[n]   = 1
                rest_n_st   = n+1
                break
    for i in stop_flag:
        if i == 1:
            print("Yes")
        else:
            print("No")

def D():
    import itertools
    N   = int(input())
    A   = [[int(a) for a in input().split()] for a in range(2*N-1)]
    point = []
    # 多分深いネストが必要な組み合わせ作るやつだ．無理．
        
D()