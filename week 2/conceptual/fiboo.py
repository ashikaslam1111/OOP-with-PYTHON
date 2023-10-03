def Fibo(N):
    def fibo(n):
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        return fibo(n - 1) + fibo(n - 2)
    lis = [fibo(i) for i in range(N+1)]
    return lis
if __name__=="__main__":
 print(Fibo(10))
 print("hello all doone")
