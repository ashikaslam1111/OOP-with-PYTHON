dp = [0]*100


def fib(n):
    if n <= 1:
        dp[n] = 0
        return dp[n]
    if n == 2:
        dp[n] = 1
        return dp[n]
    if dp[n] != 0:
        return dp[n]
    dp[n] = fib(n-1) + fib(n-2)
    return dp[n]


a = int(input())
x = fib(a)
for i in range(1,a+1):
    print(dp[i], end=" ")
