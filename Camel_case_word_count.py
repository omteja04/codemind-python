s=input()
count=1
for c in range(1,len(s)-1):
    if s[c].isupper():
        count+=1
print(count)