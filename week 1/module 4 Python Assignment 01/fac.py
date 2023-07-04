N =int(input())
dp = [0]*100000005
def fac(n):
     if n == 1:
        dp[n] = 1
        return 1
     if dp[n] != 0:
        return dp[n]
     dp[n] = n*fac(n-1)
     return dp[n]
s=str((fac(N)))
print(s)
tota=0
for  i in s[::-1]:
    if i=='0':
        tota+=1
    else:
        print(tota)
        break

 