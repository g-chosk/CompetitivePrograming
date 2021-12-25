s   = input()
p   = input()
result  = 'No'
for i in range(len(s)):
    if i + len(p) > len(s):
        if (s[i:] + s[:len(p) - len(s) + i]) == p:
            result  = 'Yes'
    else:
        if s[i:i+len(p)] == p:
            result  = 'Yes'

print(result)