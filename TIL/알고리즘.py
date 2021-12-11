https://github.com/ndb796/python-for-coding-test 

# 스택자료구조 프링글스 통과 같다 선입후출 먼저 들어온 원소가 밑에 쌓인다

stack =[]

stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop()
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
def interval_sum(start,end):
    return prefix_sum(end)-prefix_sum(start-1)
for i in range(1,n+1):
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
## 동일한 값을 가지는 데이터가 여러 개 등장할 때 효과적 사용
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

# 계수정렬 특정 조건 매우 빠름 정수형태로 표현할때 사용가능 o(n+k)
# 모든 원소의 값이 0보다 크거나 같다고 가정
array=[7,5,9,0,3,1,6,2,9,1,4,8,0,5,2]
# 모든 범위를 포함하는 리스트 선언(모든 값은 0으로 초기화)
count=[0]*(max(array)+1)
for i in range(len9array) :
    count[array[i]]==1 # 각 데이터에 해당하는 인덱스의 값 증가

for i in range(len(count)): # 리스트에 기록된 정렬 정보 확인
    for j in range(count[i]):
        print(i,end=' ') # 띄어쓰기를 구분으로 등장한 횟수만큼 인덱스 출력

# 선택정렬 아이디어가 매우 간단
# 삽입정렬 데이터가 거의 정렬되어 있을때는 가장 빠름
# 퀵정렬   대부분의 경우에 적합
# 계수정렬 데이터의 크기가 한정되어있는 경우 매우 빠르게 작동

# 두 배열의 원소 교체
## 매번 배열 a에서 가장 작은 원소를 골라서 배열 b에서 가장 큰 원소와 교체

n,k = map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
a.sort()
b.sort(reverse=True)
for i in range(k):
    if a[i]<b[i]:
        a[i],b[i]=b[i],a[i]
    else:
        break
print(sum(a))

# dfs 깊이 우선 탐색 그래프에서 깊은 부분을 우선적으로 탐색
# 스택 자료구조 재귀함수 이용  

def dfs(graph,v,visited):
    visited[v]=True
    print(v,end='')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph,i,visited)

graph=[
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]
visited=[False]*9
dfs(graph,1,visited)

# bfs 너비 우선탐색 가까운 노드부터 우선적으로 탐색 큐 자료구조 코딩테스트 자주등장
from collections import deque

def bfs(graph, start,visited):
    queue = deque([start])
    visited[start]=True
    while queue:
        v=queue.popleft()
        print(v,end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i]=True

graph=[
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]
visited=[False]*9
bfs(graph,1,visited)

# 음료수 얼려 먹기
# dfs bfs 
def dfs(x,y):
    if x<=-1 or x>=n or y<=-1 or y>=m:
        return False
    if graph[x][y] == 0:
        graph[x][y]=1
        dfs(x-1,y)
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x,y+1)
        return True
    return False
n,m = map(int,input().split())
graph=[]
for i in range(n):
    graph.append(list(map(int,input())))

result=0
for i in range(n):
    for j in range(m):
        if dfs(i,j)==True:
            result+=1
print(result)

# 미로탈출
# bfs

def bfs(x,y):
    queue=deque()
    queue.append((x,y))
    while queue:
        x,y=queue.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx<0 or nx>=n or ny<0 or ny>=m:
                continue
            if graph[nx][ny]==0:
                continue
            if graph[nx][ny]==1:
                graph[nx][ny]=graph[x][y]+1
                queue.append((nx,ny))
    return graph[n-1][m-1]

from collections import deque
n,m=map(int,input().split())
graph=[]
for i in ragne(n):
    graph.append(list(map(int,input())))
dx=[-1,1,0,0]
dy=[0,0,1,-1]
print(bfs(0,0))

# 최단 경로 알고리즘 
## 한 지점에서 다른 한 지점까지 최단경로
## 한 지점에서 다른 모든 지점까지의 최단 경로
## 모든 지점에서 다른 모든 지점까지의 최단경로
## 다익스트라는 그리디 알고리즘으로 분류 매 상황에서 가장 비용이 적은 노드를 선택해 임의의 과정을 반복

import sys
input=sys.stdin.readline
INF=int(1e9)

n,m=map(int,input().split())
start=int(input())
graph=[[] for i in range(n+1)]
visited=[False]*(n+1)
distance=[INF]*(n+1)
for _ in range(m):
    a,b,c=map(int,input().split())
    graph[a].append((b,c))
    def get_smallest_node():
        min_value=INF
        index=0
        for i in range(1,n+1):
            if distance[i]<min_value and not visited[i]:
                min_value=distance[i]
                index=i
        return index

def dijkstra(start):
    distance[start]=0
    visited[start]=True
    for j in graph[start]:
        distance[j[0]]=j[1]
    for i in range(n-1):
        now=get_smallest_node()
        visited[now]=True
        for j in graph[now]:
            cost=distance[now]+j[i]
            if cost < distance[j[0]]:
                distance[j[0]]=cost

dijkstra(start)
for i in range(1,n+1):
    if distance[i]==INF:
        print('INFINITY')
    else:
        print(distance[i])

# 우선순위 큐 
## 우선순위가 가장 높은 데이터를 가장 먼저 삭제
## 스택 가장 나중에 삽입된 데이터
## 큐   가장 먼저 삽입된 데이터
## 우선순위큐 가장 우선순위가 높은 데이터

# 힙 라이브러리
# 최소힙
import heapq
def heapsort(iterable):
    h=[]
    result=[]
    for value in iterable:
        heapq.heappush(h,value)
    for i in range(len(h)):
        result.append(heapq.heappop(h))
    return result
result =heapsort([1,3,5,7,9,2,4,6,8,0])
print(result)

#최대힙
import heapq
def heapsort(iterable):
    h=[]
    result=[]
    for value in iterable:
        heapq.heappush(h,-value)
    for i in range(len(h)):
        result.append(-heapq.heappop(h))
    return result
result =heapsort([1,3,5,7,9,2,4,6,8,0])
print(result)

#다익스트라 알고리즘
import heapq
import sys
input=sys.stdin.readline
INF-int(1e9)

n,m=map(int,input().split())
start=int(input())
graph=[[] for i in range(n+1)]
distance=[INF]*(n+1)
for _ in range(m):
    a,b,c=map(int,input().split())
    graph[a].append((b,c))

def dijkstra(start):
    q=[]
    heapq.heappush(q,(90,start))
    distance[start]=0
    while q:
        dist,now = heapq.heappop(q)
        if distance[now]<dist:
            continue
        for i in graph[now]:
            cost = dist+i[1]
            if cost,distance[i[0]]:
                distance[i[0]]=cost
                heapq.heappush(q,(cost,i[0]))

dijkstra(start)
for i in range(1,n+1):
    if distance[i]==INF:
        print('INFINITY')
    else:
        print(distance[i])

# 플로이드 워셜 알고리즘
## 모든 노드에서 다른 모든 노드까지의 최단 경로를 모두 계산
## 2차원 테이블, 다이나믹 프로그래밍 유형

## Dab=min(Dab,Dak+Dkb)

INF=int(1e9)
n=int(input())
m=int(input())
graph=[[INF]*(n+1)for _ in range(n+1)]
for a in range(1,n+1):
    for b in range(1,n+1):
        if a==b:
            graph[a][b]=0

for _ in range(m):
    a,b,c=map(int,input().split())
    graph[a][b]=c

for k in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            graph[a][b]=min(graph[a][b],graph[a][k]+graph[k][b])

for a in range(1,n+1):
    for b in range(1,n+1):
        if graph[a][b]==INF:
            print('INFINITY',end=' ')
        else:
            print(graph[a][b],end=' ')
    print()

## o(n3)

# 벨만 포드 알고리즘
# boj 타임머신 https://www.acmicpc.net/problem/11657






