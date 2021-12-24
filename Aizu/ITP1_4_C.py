A,O,B   = [],[],[]
while 1:
    a,op,b  = input().split()
    if str(op) == "?":
        break
    else:
        A.append(int(a))
        B.append(int(b))
        O.append(str(op))
for (a,op,b) in zip(A,O,B):
    if op == "+":
        print(a+b)
    elif op == "-":
        print(a-b)
    elif op == "*":
        print(a*b)
    elif op == "/":
        print(a//b)