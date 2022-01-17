n   = int(input())
Taro_point  = 0
Hanako_point    = 0

for i in range(n):
    even_flag = 1
    taro,hanako   = input().split()
    taro    = taro.lower()
    hanako  = hanako.lower()
    for j in range(min(len(taro),len(hanako))):
        if taro[j] > hanako[j]:
            Taro_point += 3
            even_flag = 0
            break
        elif hanako[j] > taro[j]:
            Hanako_point += 3
            even_flag = 0
            break
        else:
            pass
    
    if even_flag:
        if len(taro) > len(hanako):
            Taro_point += 3
        elif len(hanako) > len(taro):
            Hanako_point += 3
        else:
            Taro_point += 1
            Hanako_point += 1
print(Taro_point, Hanako_point)