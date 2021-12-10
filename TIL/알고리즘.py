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

복잡도 o(NlogN)

# HEAP
## 완전 이진트리 항상 루트노드를 제거
## 최소힙 루트 노드가 가장 작은 값을 가진다 값이 작은 데이터가 우선적으로 제거
## 최대힙 루트 노드가 가장 큰 값을 가진다 값이 큰 데이터가 우선적으로 제거
## 오름차순으로 출력

import sysimport heapq
input = sys.stdin.realine

def heapsort(iterable):
    h=[]
    resul=[]
    for value in iterable:
        heapq.heappush(h,value)
    for i in range(len(h)):
        result.append(heapq.heappop(h))
    result result

n=int(input())
arr=[]
for i in range(n):
    arr.append(int(input()))

res=heapsort(arr)
for i in range(n):
    print(res[i])

# 트리
## 루트노드 부모없는 최상위 노드  단군할아버지 깊이 0
## 단말노드 자식이 없는 노드  가장 아래쪽 
## 크기     트리에 포함된 모든 노드의 개수
## 깊이     루트 노드부터의 거리
## 높이     깊이 중 최댓값
## 차수     각 노드의 자식방향 간선 개수
## 기본적으로 트리의 크기가 n일때 전체 간선 개수는 n-1

# 이진탐색트리
## 특징 : 왼쪽자식노드<부모노드<오른쪽자식노드
## 부모노드보다 왼쪽자식노드가 작다
## 부모노드보다 오른쪽자식노드가 작다
## 이걸 노드마다 반복

#트리의 순회
## 트리 자료구조에 포함된 노드를 특정한 방법으로 한 번씩 방문하는 방법을 의미 트리의 정보를 시각적으로 확인가능
## 전위 순회 루트를 먼저 방문
## 중위 순회 왼쪽 자식을 방문한 뒤 루트를 방문
## 후위 순회 오른쪽 자식을 방문한 뒤에 루트를 방문

class Node:
    def __init__(self,data,left_node,right_node):
        self.data=data
        self.left_node=left_node
        self.right_node=right_node

# 전위순회
def pre_order(node):
    print(node.data, end=' ')
    if node.left_node!=None:
        pre_order(tree[node.left_node])
    if node.right_node!=None:
        pre_order(tree[node.right_node])

# 중위순회
def in_order(node):
    if node.left_node!=None:
        in_order(tree[node.left_node])
    print(node.data,end=' ')
    if node.right_node!=None:
        in_order(tree[node.right_node])

# 후위순회
def post_order(node):
    if node.left_node!=None:
        post_order(tree[node.left_node])
    if node.right_node!=None:
        post_order(tree[node.right_node])
    print(node.data, end=' ')

n=int(input())  # 노드의 개수 
tree={}

for i in range(n):
    data,left_node,right_node=input().split()
    if left_node=='None':
        left_node=None
    if right_node=='None':
        right_node=None
    tree[data]=Node(data,left_node,right_node)

pre_order(tree['A'])
print()
in_order(tree['A'])
print()
post_order(tree['A'])

# BOJ 구간합구하기 문제 https://www.acmicpc.net/problem/2042
# 바이너리 인덱스 트리 2진법 인덱스 구조
## 펜윅 트리
## 특정한 숫자 k의 0이 아닌 마지막 비트 k &-k
for i in range(n+1):
    print(i,'의 마지막 비트:',(i &-1))
