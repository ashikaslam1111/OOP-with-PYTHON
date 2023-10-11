n = int(input())
ar = list(map(int, input().split()))
ar1=[]
for i in range(n):
    ar1.append((ar[i],i))
ar1.sort()
ans = 1
for i in range(1,n):
    if ar1[i][1]<ar1[i-1][1]:ans+=1
print(ans)