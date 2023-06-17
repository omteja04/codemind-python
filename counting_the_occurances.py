string=input()
char=input()
c=0
for i in string:
    if i==char:
        c+=1
if c==0:
    print(-1)
else:
    print(c)