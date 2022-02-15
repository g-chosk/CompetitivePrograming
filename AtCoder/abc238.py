
def a():
    n = int(input())
    if n < 10:
        if 2**n > n**2:
            print("Yes")
        else:
            print("No")
    else:
        print("Yes")

def B():
    N   = int(input())
    A   = [int(x) for x in input().split()]
    for i in range(N):
        if i == 0:
            A[i]    = A[i] + 0
        else:
            A[i]    = A[i] + A[i-1]
        if A[i] >= 360:
            A[i] = A[i] %360
    A   = sorted(A)
    max_theta = 0
    theta   = [(x - y) for (x,y) in zip((A + [360]) , ([0]+A))]
    print(max(theta))


def C():
    N   = int(input())
    order = len(str(N))-1
    ans = 0
    for i in range(order):
        n   = 9*10**i
        ans = ans +  n*(1+n)/2
    n = N-10**order+1
    ans = ans + n*(1+n)/2
    print(int(ans % 998244353))
    #  /2 と，//2がおかしい．n(n+1)/2とn(n+1)//2は同じだと思うが，結果が異なってくる．

    mod=998244353
    n=int(input())
    ans=0
    for i in range(1,19):
        low=pow(10,i-1)
        high=pow(10,i)-1
        l = max(0,min(high,n)-max(low,1)+1)
        ans = (ans + l*(l+1)//2)%mod
    print(ans)
C()