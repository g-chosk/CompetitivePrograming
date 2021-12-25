Str = input()
for i in Str:
    if i.islower():
        i   = i.upper()
    elif i.isupper():
        i   = i.lower()
    else:
        pass
    print("%s"%i,end='')
print()