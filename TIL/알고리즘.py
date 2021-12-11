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

## 트리 구조 만들기 0이 아닌 마지막 비트 내가 저장하고 있는 값들의 개수
## 특정 값을 변경할 때 0이 아닌 마지막 비트만큼 더하면서 구간들의 값을 변경 3,4,8,16 logn 보장
## 1부터 n까지의 누적합 구하기 0이 아닌 마지막 비트만큼 빼면서 구간들의 합계산 11부터 출발 11 10 8

import sys
input = sys.stdin.readline

# 데이터의 개수n 변경횟수m 구간 합 계산 횟수k
n,m,k = map(int(input).split())

# 전체 데이터의 개수는 최대 1,000,000개
arr =[0]*(n+1)
tree = [0]*(n+1)

# i번쨰 수까지의 누적 합을 계산하는 함수
def prefix_sum(i):
    result=0
    while i>0:
        result +=tree[i]
        i-=(i &-1)
    return result

# i번째 수를 dif만큼 더하는 함수
def update(i,dif):
    while i <=n:
        tree[i] += dif
        i+=(i &-1)

# start부터 end까지의 구간합을 계산하는 함수 
def inerval_sum(start,end):
    return prefix_sum(end)-prfix_sum(start-1)
for i in ragne(1,n+1):
    x = int(input())
    arr[i]=x
    update(i,x)

for i in range(m+k):
    a,b,c=map(int,input().split())
    #업데이트 연산인 경우
    if a==1:
        update(b,c-arr[b])# 바뀐 크기의(dif)만큼 적용
        arr[b]=c
    # 구간 합(interval sum) 연산인 경우
    else:
        print(interval_sum(b,c))
    
# 정렬 알고리즘 데이터를 특정한 기준에 따라 순서대로 나열 
## 처리되지 않은 데이터 중에서 가장 작은 데이터를 선택해 맨 앞에 있는 데이터와 바꾸는 것을 반복

array=[7,5,9,0,3,1,6,2,4,8]
for i in range(len(array)):
    min_index=i # 가장 작은 원소의 인덱스
    for j in ragne(i+1,len(array)):
        if array[min_index]>array[j]:
            min_index=j
    array[i], array[min_index]=array[min_index],array[i] #스와프
print(array)

# 이는 (n2(제곱)+n-2)/2 로 표현 빅오 표기법에 따라 'o(n2(제곱))'

# 삽입 정렬 처리되지 않은 데이터를 하나씩 골라 적절한 위치에 삽입 일반적으로 더 효율적 

array=[7,5,9,0,3,1,5,2,4,8]
for i in range(1,len(array)):
    for j in range(i,0,-1): # 인덱스 i부터 1까지 1씩 감소하며 반복하는 문법
        if array[j]<array[j-1]: # 한 칸씩 왼쪽으로 이동
            array[j],array[j-1]=array[j-1],array[j]
        else:
            break
print(array)

최선의 경우 0(n)만큼의 시간 복잡도를 가진다 

# 퀵 정렬 기준데이터를 설정하고 그 기준보다 큰 데이터와 작은 데이터의 위치를 바꾸는 방법 가장 일반적
## 병합정렬과 더불어 근간이 되는 알고리즘
## 첫번째 데이터를 기준 데이터로 설정
## 피봇값을 중심으로 분할 재귀적 진행될수록 범위 좁아짐 o(nlogn) 피봇값 설정이 중요

array =[5,7,9,0,3,1,6,2,4,8]
def quick_sort(array,start,end):
    if start>=end: # 원소가 1개인 경우 종료
        return
    pivot=start
    left=start+1
    right=end
    while(left<=right):
        #피벗보다 큰 데이터를 찾을 때까지 반복
        while(left<=end and array[left]<=array[pivot])
        #피벗보다 작은 데이터를 찾을 때까지 반복
        while(right>start and array[right]>=array[pivot]):
            right-=1
        if(left>right):# 엇갈렸다면 작은 데이터와 피벗을 교체
            array[right],array[pivot]=array[pivot,],array[right]
        else: # 엇갈리지 않았다면 작은 데이터와 큰 데이터를 교체
            array[left],array[right]=array[right],array[left]
    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행
    quick_sort(array,start,right-1)
    qucik_sork(array,right+1,end)
quick_sort(array,0,len(array)-1)
print(array)

# 퀵 정렬 소스코드 파이썬의 장점을 살린 방식
array=[5,7,9,0,3,1,6,2,4,8]
def quick_sort(array):
    # 리스트가 하나 이하의 원소만을 담고 있다면 종료
    if len(array)<=1:
        pivot =array[0]# 피벗은 첫 번째 원소
        tail=array[1:]#피벗을 제외한 리스트
        left_side=[x for x in tail if x <=pivot] # 분할된 왼쪽 부분
        right_side=[x for x in tail if x > pivot] # 분할된 오른쪽 부분

        #분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행하고 전체 리스트 반환
        return quick_sort(left_side)+[pivot]+quick_sort(right_side)
print(quick_sort(array))

