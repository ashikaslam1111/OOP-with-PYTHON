from collections import deque

stack = deque()
stack.append(1)
stack.append(2)
stack.append(3)
stack.append(4)
stack.append(5)
print(stack[-1])
stack.pop()
print(stack[-1])
print(len(stack)+100)
