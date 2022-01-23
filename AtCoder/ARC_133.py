# unratedで参加．

def A():
    # 結局例外を見つけられるかどうかだった．
    # 結果がWAであっても内訳はWA1つとかだったから，例外を見つけられていないと考えた．
    N   = int(input())
    A   = [int(a) for a in input().split()]
    if N == 1:
        print()
    else:
        for i in range(len(A)-1):
            if i == len(A) - 2:
                A   = [item for item in A if item != A[i+1]]
                break
            else:
                if A[i] > A[i+1]:
                    A   = [item for item in A if item != A[i]]
                    break
                else:
                    pass
        for i in A:
            print(i,end=' ')
if __name__ == "__main__":
    A()