Array   = []
while 1:
    m,f,r   = map(int,input().split())
    if (m,f,r) == (-1,-1,-1):
        break
    else:
        Array.append([m,f,r])

for i in Array:
    m,f,r   = i
    if m==-1 or f==-1:
        print("F")
    elif m+f >= 80:
        print("A")
    elif m+f >= 65 and m+f < 80:
        print("B")
    elif m+f >= 50 and m+f < 65:
        print("C")
    elif m+f >= 30 and m+f < 50:
        if r>=50:
            print("C")
        else:
            print("D")
    elif m+f<30:
        print("F")