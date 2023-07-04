n = int(input())
l = list(map(int, input().split()))
def solve(lst):
    op=0
    while 1:
        for i in lst:
            if i%2!=0:
                return op
        op+=1
        lst = list(map(lambda x:x/2,lst))
print(solve(l))

 