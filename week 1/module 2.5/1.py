
t = int(input())
while t:
    s = input()
    n = len(s)
    
    for i in range(n-1, -1, -1):
        print(s[i],end=' ') 
    print()  
    t-=1