import math
n   = int(input())
x_set   = [int(x) for x in input().split()]
y_set   = [int(y) for y in input().split()]

for p in [1,2,3]:
    Dxy = 0
    for (x,y) in zip(x_set, y_set):
        Dxy += abs(x - y)**p
    Dxy = Dxy ** (1/p)
    print(Dxy)

Dxy8    = 0
for (x,y) in zip(x_set, y_set):
    Dxy8    = max(Dxy8, abs(x - y))
print(Dxy8)