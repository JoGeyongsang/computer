# 스택자료구조 프링글스 통과 같다 선입후출 먼저 들어온 원소가 밑에 쌓인다

stack =[]

stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop
stack.append(1)
stack.append(4)
stack.pop()

print(stack[::1]) #최상단 원소부터 출력
print(stack) #최하단 원소부터 출력

# 큐 자료구조 입구 출구 모두 뚫려있는 터널 선입선출

from collections import deque

queue = deque()

queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()
queue.append(1)
queue.append(4)
queue.popleft()

print(queue)
queue.reverse()
print(queue)

# 우선순위 큐 우선순위가 가장 높은 데이터를 가장 먼저 삭제함