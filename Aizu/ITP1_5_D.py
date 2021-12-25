n   = int(input())
for i in range(1,n+1,1):
    x   = i
    if x%3 == 0:
        print(" %d"%i,end='')
    else:
        flag    = True
        while flag:
            if x%10 == 3:
                print(" %d"%i, end='')
                flag    = False
            else:
                x   /= 10
                x   = int(x)
                flag    = (x!=0)