n=int(input())
arr=list(map(int,input().split()))
hcf=arr[n-1]
i=0
while i<n-1:
    if arr[i]%hcf==0:
        i+=1
    else:
        hcf=arr[i]%hcf
print(hcf)