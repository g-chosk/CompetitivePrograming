W   = input()
T   = []
while 1:
    t   = input()
    T.append(t.split())
    if "END_OF_TEXT" in t:
        break
print(T)