counter = [0 for i in range(26)]

while 1:
    try:
        Sentence    = input()
    except EOFError:
        break

    for s in Sentence:
        if s.isupper:
            s   = s.lower()
        num = ord(s) - ord("a")
        if ord(s) >= ord("a") and ord(s) <= ord("z"):
            counter[num]    += 1

for i in range(len(counter)):
    s   = chr(i + ord("a"))
    print("%s : %d"%(s,counter[i]))