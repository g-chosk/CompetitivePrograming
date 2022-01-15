strings = []
ms  = []
hs  = []
j   = 0
while 1:
    string  = input()
    if string == '-':
        break
    else:
        strings.append(string)
        m   = int(input())
        ms.append(m)
        hs.append([int(input()) for i in range(m)])
        j   += 1
for i in range(len(strings)):
    for j in hs[i]:
        strings[i]  = strings[i][j:] + strings[i][:j]
for s in strings:
    print(s)