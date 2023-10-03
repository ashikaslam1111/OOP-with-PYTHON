from collections import deque
q = deque()
q.appendleft(1)
q.appendleft(10)
q.appendleft(100)
q.appendleft(1000)
print(q[-1])
q.pop()
print(q[-1])


