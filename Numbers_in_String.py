string =input()
c=0
for i in string:
    if i.isdigit():
        c+=int(i)
print(c)