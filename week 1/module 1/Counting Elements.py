n = int(input())
res =0
lst = list(map(int, input().split()))
for i in lst:
    if i+1 in lst:
     res+=1
print(res)





