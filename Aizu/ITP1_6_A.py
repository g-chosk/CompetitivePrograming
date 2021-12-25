n   = int(input())
a   = [int(x) for x in input().split()]
for i in range(len(a)):
    if i != len(a) - 1:
        print(a[-i-1],end=' ')
    else:
        print(a[-i-1])