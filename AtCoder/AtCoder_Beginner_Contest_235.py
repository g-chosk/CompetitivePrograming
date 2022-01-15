from itertools import count
from tkinter import N


def A():
    N   = str(input())
    print(int(N) + int(N[1]+N[2]+N[0]) + int(N[2]+N[0]+N[1]))

def B():
    N   = int(input())
    H   = [int(h) for h in input().split()]
    result  = H[0]
    for i in range(N-1):
        if H[i] < H[i+1]:
            result  = H[i+1]
        else:
            break
    print(result)
#B()

def C():
    N,Q = [int(i) for i in input().split()]
    a_set   = [int(i) for i in input().split()]
    x_set   = [0]*Q
    k_set   = [0]*Q
    for q in range(Q):
        x_set[q],k_set[q]   = [int(i) for i in input().split()]
    a_organized = {}
    for i in range(N):
        try:
            a_organized[a_set[i]].append(i)
        except:
            a_organized[a_set[i]]   = [i]
    for i in range(Q):
        try:
            print(a_organized[x_set[i]][k_set[i]-1]+1)
        except:
            print(-1)
#C()

def D():
    # できてない。木構造ってやつかと思い、幅優先の深さを探せば良いと思った。
    a,N = [int(i) for i in input().split()]
    operation   = 0
    KOKUBAN_now = [1]
    KOKUBAN_next    = []
    break_flag=0
    while 1:
        operation   += 1
        for x in KOKUBAN_now:
            x_next1  = a*x
            if x_next1 == N:
                break_flag = 1
            elif x_next1 > N*a:
                break_flag = 2
            else:
                KOKUBAN_next.append(x_next1)
            if x>10 and x%10!=0:
                x_next2  = int(str(x)[-1]+str(x)[:-1])
                if x_next2  == N:
                    break_flag  = 1
                elif x_next2 > N*a:
                    break_flag = 2
                else:
                    KOKUBAN_next.append(x_next2)
        print(operation)
        if break_flag == 1:
            print(operation)
            break
        KOKUBAN_now = KOKUBAN_next
        KOKUBAN_next    = []
D()