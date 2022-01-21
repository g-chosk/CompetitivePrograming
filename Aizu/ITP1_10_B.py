import math
a,b,C   = [float(i) for i in input().split()]
S   = 1/2*a*b*math.sin(C/180*math.pi)
c   = math.sqrt(a**2+b**2-2*a*b*math.cos(C/180*math.pi))
L   = a+b+c
h   = 2*S/a
print(S,L,h)