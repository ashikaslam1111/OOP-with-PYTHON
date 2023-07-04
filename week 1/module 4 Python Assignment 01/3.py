n = int(input())
l = list(map(int, input().split()))
toTaa = 0
temp = l
for i in temp:
    if temp.count(i) != i:
        if temp.count(i) < i:
            toTaa += temp.count(i)
            while i in temp:
                temp.remove(i)
        elif temp.count(i) > i:
            toTaa += temp.count(i)-i
            while i in temp:
                temp.remove(i)
print(toTaa)

