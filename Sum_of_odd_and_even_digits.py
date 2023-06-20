n=int(input())
arr=list(map(int,input().split()))
es=0
os=0

for i in range(0,n,2):
    es+=arr[i]
for i in range(1,n,2):
    os+=arr[i]
if abs(os-es==0):
    print("YES")
else:
    print("NO")