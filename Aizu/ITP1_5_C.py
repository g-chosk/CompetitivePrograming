H,W = [],[]
while 1:
    h,w = map(int,input().split())
    if (h,w) == (0,0):
        break
    else:
        H.append(h)
        W.append(w)
for (h,w) in zip(H,W):
    for i in range(h):
        if i%2 == 0:
            print("#."*(w//2) + "#"*(w%2))
        else:
            print(".#"*(w//2) + "."*(w%2))
    print()