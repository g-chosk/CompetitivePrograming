r,c = [int(x) for x in input().split()]
Array   = [[0 for i in range(c+1)]for j in range(r+1)]
for i in range(r):
    Array[i][:c]    = [int(x) for x in input().split()]
for i in range(r):
    for j in range(c):
        Array[i][c] += Array[i][j]
        Array[r][j] += Array[i][j]
for i in range(c):
    Array[r][c] += Array[r][i]

for i in Array:
    for j in range(len(i)):
        if j != len(i) -1:
            print("%d "%i[j],end='')
        else:
            print("%d"%i[j])