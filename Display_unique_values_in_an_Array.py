n=int(input())
arr=list(map(int,input().split()))
arr1=[]
for i in arr:
    if arr.count(i)==1:
        arr1.append(i)
if len(arr1)!=0:
    print(*arr1)
else:
    print(-1)
        