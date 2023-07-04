
n = int(input())
for i in range(1, n*2, 2):
    for s in range(1, (n*2-i)//2):
            print(end=" ")
    for st in range(1, i+1):
        print('*', end="")
    print()
