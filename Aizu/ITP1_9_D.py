Str = input()
q   = int(input())
output  = []
for i in range(q):
    command_line    = input().split()
    command_now = command_line[0]
    a,b = [int(x) for x in command_line[1:3]]
    if command_now  == "print":
        output.append(Str[a:b+1])
    elif command_now == "reverse":
        Str = Str[:a] + Str[a:b+1][::-1] + Str[b+1:]
    elif command_now == "replace":
        p   = command_line[3]
        Str = Str[:a] + p + Str[b+1:]
if output != []:
    for s in output:
        print(s)