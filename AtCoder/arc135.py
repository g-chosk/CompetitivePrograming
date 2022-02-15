def a():
    import math
    X = int(input())
    value = list([X])
    num = list([1])
    while 1:
        x = max(value)
        N = num[value.index(x)]
        Index = value.index(x)
        if x == 2 or x == 3 or x == 4 or x == 1:
            break
        else:
            x_floor = math.floor(x//2 + (x%2)/2)
            x_ceil = math.ceil(x//2 + (x%2)/2)
            if x_floor in value:
                num[value.index(x_floor)] += N
            else:
                value.append(x_floor)
                num.append(N)
            if x_ceil in value:
                num[value.index(x_ceil)] += N
            else:
                value.append(x_ceil)
                num.append(N)
            del(value[Index])
            del(num[Index])
    Product = 1

    if 2 in value:
        Product *= pow(2,num[value.index(2)],998244353)
    if 3 in value:
        Product *= pow(3,num[value.index(3)],998244353)
    if 4 in value:
        Product *= pow(4,num[value.index(4)],998244353)
    print(Product%998244353 )
a()

from functools import lru_cache

MOD = 998244353

@lru_cache
def f(X):
    if X <= 4:
        return X
    X1 = X // 2
    X2 = (X + 1) // 2
    return f(X1) * f(X2) % MOD

X = int(input())
print(f(X))

