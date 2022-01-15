W   = input()
T   = [""]
while 1:
    t   = input()
    for t_ in t.split():
        T.append(t_.lower())
    if "END_OF_TEXT" in t:
        break
print(T.count(W))