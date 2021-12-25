n   = int(input())
Array   = []
for i in range(n):
    Array.append(input().split())
for x in ["S","H","C","D"]:
    for i in range(1,14,1):
        if [x,str(i)] in Array:pass
        else:
            print(x,i)