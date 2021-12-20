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
from typing import no_type_check

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
## 음수 간선 순환이 있는 경우도 사용 가능 음수 간선의 순환 감지
## O(VE)

# 다익스트라 알고리즘 음수간선없다면 최적의 해를 찾을 수 있다
# 벨만 포드 알고리즘 다익스트라 알고리즘에서의 최적의 해를 항상 포함 시간은 오래 걸리지만 음수간선 탐지 가능

import sys
input=sys.stdin.readline
INF=int(1e9)
def bf(start):
    dist[start]=0
    for i in range(n):
        for j in range(m):
            cur = edges[j][0]
            next_node=edges[j][1]
            cost=edges[j][2]
            if dist[cur]!=INF and dist[next_node]>dist[cur]+cost:
                dist[next_node]=dist[cur]+cost
                if i==n-1:
                    return True
    return False

n,m=map(int,input(0.split()))
edges=[]
dist=[INF]*(n+1)
for _ in range(m):
    a,b,c=map(int,input().split())
    edges.append((a,b,c))
negative_cycle=bf(1)
if negative_cycle:
    print('-1')
else:
    for i in range(2,n+1):
        if dist[i]==INF:
            print('-1')
        else:
            print(dist[i])

# 서로소 집합 공통원소가 없는 두 집합 
# 서로소 집합 자료구조는 합치기 찾기 자료구조
# 서로소 집합 자료구조
def find_parent(parent,x):
    if parent[x]!= x:
        return find_parent(parent,parent[x])
    return x

def union_parent(parent,a,b):
    a=find_parent(parent,a)
    b=find_parent(parent,b)
    if a<b:
        parent[b]=a
    else:
        parent[a]=b
v,e =map(int,input().split())
parent=[0]*(v+1)
for i in ragne(1,v+1):
    parent[i]=i
for i in range(e):
    a,b=map(int,input().split())
    union_parent(parent,a,b)
print('각 원소가 속한 집합: ', end=' ')
for i in range(1,v+1):
    print(find_parnetn(parent,i),end=' ')

print()

print('부모테이블: ',end=' ')
for i in range(1,v+1):
    print(parent[i],end=' ')

# 경로압축
# 특정 원소가 속한 집합을 찾기
def find_parent(parent,x):
# 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x]!=x:
        parent[x]=find_parent(parent,parent[x])
    return parent[x]

# 서로소 집합은 무방향 그래프 내에서 사이클을 판별할때 사용
# 서로소 집합을 활용한 사이클 판별
def find_parent(parent,x):
    if parent[x]!=:
        parent[x]=find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent,a,b):
    a=find_parent(parent,a)
    b=find_parent(parent,b)
    if a<b:
        parent[b]=a
    else:
        parent[a]=b

v,e = map(int,input().split())
parent=[0]*(v+1)
for i in range(1,v+1):
    parent[i]=i
cycle = False
for i in range(e):
    a,b=map(int,input().split())
    if find_parent(parent,a)==find_parent(parent,b):
        cycle=True
        break
    else:
        union_parent(parent,a,b)
if cycle:
    print('사이클이 발생했습니다')
else:
    print('사이클이 발생하지 않았습니다')

# 신장트리 그래프에서 모든 노드를 포함하면서 사이클이 존재하지 않는 부분 그래프
# 최소신장트리 두 도시 a,b를 선택했을 때 a에서 b로 이동하는 경로가 반드시 존재하도록 도로를 설치
# 크루스칼 알고리즘 그리디 알고리즘
## 간선데이터를 비용에 따라 오름차순으로 적용 간선을 하나씩 확인하여 사이클이 발생하는지 확인
## 최소신장트리에 포함되어있는 간선의 비용을 모두 더하면 최종비용이 됨

def find_parent(parent,x):
    if parent[x]!=x:
        parent[x]=find_parent(parent,parent[x])
    return paretn[x]

def union_parent(parent,a,b):
    a=find_parent(parent,a)
    b=find_parent(parent,b)
    if a<b:
        parent[b]=a
    else:
        paretn[a]=b

v,e=map(int,input().split())
edges=[]
result=0

for i in range(1,v+1):
    parent[i]=i
for _ in range(e):
    a,b,cost=map(int,input().split())
    edges.append((cost,a,b))
edges.sort()
for edge in edges:
    cost,a,b=edge
    if find_parent(parent,a)!=find_parent(parent,b):
        union_parent(parent,a,b)
        result+=cost
print(result)

# 크루스칼 알고리즘 간선의 개수가 E개일때 O(ELOGE)의 시간복잡도 

# 최소공통조상
# boj lca문제 https://www.acmicpc.net/problem/11437
## 최소공통조상 알고리즘 lca 
### 먼저 두 노드의 깊이를 맞춘다 이후 거슬로 올라간다

import sys
sys.setrecusionlimit(int(1e5))
n=in(input())
parent=[0]*(n+1)
d=[0]*(n+1)
c=[0]*(n+1)
graph=[[] for _ in range(n+1)]

for _ in range(n-1):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(x,depth):
    c[x]=True
    d[x]=depth
    for y in graph[x]:
        if c[y]:
            continue
        parent[y]=x
        dfs(y,depth+1)

def lca(a,b):
    while d[a]!=d[b]:
        if d[a]>d[b]:
            a=parent[a]
        else:
            b=parent[b]
    while a!=b:
        a=parent[a]
        b=parent[b]
    return a

dfs(1,0)
m=int(input())
for i in range(m):
    a,b=map(int,input().split())
    print(lca(a,b))

# lca 시간복잡도 O(NM)

# lca 심화문제 https://www.acmicpc.net/problem/11438
## 시간복잡도 O(mlogn)
## 먼저 두 노드의 깊이를 맞춘다 이후에 거슬로 올라간다 

import sys
input=sys.stdin.readline
sys.setrecusionlimint(int(1e5))
LOG=21#2^20=1,000,000

n=int(input())
parent+[[0]*LOG for _ in range(n+1)]
d=[0]*(n+1)
c=[0]*(n+1)
graph=[[] for _ in range(n+1)]
for _ in range(n-1):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(x,depth):
    c[x]=True
    d[x]=depth
    for y in graph[x]:
        if c[y]:
            continue
        parent[y][0]=x
        dfs(y,depth+1)

def set_parent():
    dfs(1,0)
    for i in range(1,LOG):
        for j in range(1,n+1):
            parent[j][i]=parent[parent[j][i-1][i-1]]

def lca(a,b):
    if d[a]>d[b]:
        a,b=b,a
    for i in range(LOG-1,-1,-1):
        if d[b]-d[a]>=(1<<i):
    if a==b:
        return a;
    for i in range(LOG-1,-1,-1):
        if parent[a][i]!=parent[b][i]:
            a=parent[a][i]
            b=parent[b][i]
    return parent[a][0]
set_parent()
m=int(input())
for i in range(m):
    a,b=map(int,input().split())
    print(lca(a,b))

# 위상정렬 
## 사이클이 없는 방향 그래프의 모든 노드를 방향성에 거스르지 않도록 순서대로 나열 dhe
## 선수과목을 고려한 학습 순서 설정
## 진입차수 특정한 노드로 들어오는 간선의 개수
## 진출차수 특정한 노드에서 나가는 간선의 개수 
## 사이클이 없는 방향 그래프(dag)여야 한다
## 진입차수가 0인 모든 노드를 큐에 넣는다 
## 큐에서 노드1을 꺼낸 뒤에 노드 1에서 나가는 간선제거 새롭게 진입차수가 이 된 노드들을 큐에 삽입
## 위상정렬은 순환하지 않느 방향그래프(dag)에 대해서만 수행 여러가지답이 존재
 
from collections import deque
v,e=map(int,input().split())
indegree=[0]*(v+1)
graph=[[] for i in range(v+1)]
for _ in range(e):
    a,b=map(int,input().split())
    graph[a].append(b)
    indegree[b]+=1

def topology_sort():
    result=[]
    q=deque()
    for i in range(1,v+1):
        if indegree[i]==0:
            q.append(i)
    while q:
        now=q.popleft()
        result.append(now)
        for i in range[now]:
            indegree[i]-=1
            if indegree[i]==0:
                q.append(i)
    for i in result:
        print(i,end=' ')
topology_sort()

## 시간복잡도 O(V+E)

# 재귀함수 자기 자신을 다시 호출하는 함수 DFS
## 종료조건을 포함한 재귀함수
def recursive_function(i):
    if i ==100:
        return
    print(i, '번째 재귀함수에서',i+1,'번째 재귀함수를 호출합니다')
    recursive_function(i+1)
    print(i,'번째 재귀함수를 종료합니다')
recursive_function(1)

# 팩토리얼 구현
def factorial_iterative(n):
    result=1
    for i in range(i,n+1):
        result*=i
    return result

def factorial_recursive(n):
    if n<=1:
        return 1
    return n *factorial_recursive(n-1)
print('반복적으로 구현: ',factorial_iterative(5))
print('재귀적으로 구현: ',factorial_recursive(5))

# 최대공약수 계산 유클리드 호제법 
def gcd(a,b):
    if a%b==0:
        return b
    else:
        return gcd(b,a%b)
print(gcd(192,162))

## 모든 재귀함수는 반복문을 이용하여 동일한 기능을 구현
## 스택을 사용해야 할 때 스택 라이브러리 대신에 재귀함수를 이용하는 경우가 많다

# 유용한 표준 라이브러리

## 내장함수 
## itertools 순열 조합 라이브러리
## heapq     힙 자료구조 우선순위 큐 기능
## bisect    이진탐색기능
## collections 덱 카운터 등의 유용한 자료구조 
## math      필수적인 수학적 기능 팩토리얼 제곱근 최대공약수 삼각함수 파이 

# sum()
result=sum([1,2,3,4,5])
print(print(result))

# min(),max()
min_result=min(7,3,5,2)
max_result=max(7,3,5,2)
print(min_result,max_result)

# eval()  계산한 결과를 수형태로 반환 
result=eval('(3+5)*7')
print(result)

# sorted()
result=sorted([9,1,8,5,4])
reverse_result=sorted([9,1,8,4,5],reverse=True)
print(result)
print(reverse_result)

# sorted()with key
array=[('홍길동',35),('이순신',75),('아무개',50)]
result=sorted(array,key=lambda x: x[1],reverse=True)
print(result)

# 순열 nPr 서로 다른 n개에서 서로다른 r개를 선택해 일렬로 나열
# 조합 nCr 서로 다른 n개에서 순서 상관없이 서로 다른 r개를 선택해 나열

# 순열 
from itertools import permutations
data=['A','B','C']
result=list(permutations(data,3))
print(result)

# 조합
from itertools import combinations
data=['A','B','C']
result=list(combinations(data,2))
print(result)

# 중복순열
from itertools import product
data=['A','B','C']
result=list(product(data,repeat=2))
print(result)

# 중복조합
from itertools import combinations_with_replacement
data=['A','B','C']
result=list(combinations_with_replacement(data,2))
print(result)

# counter 등장 회수를 세는 기능
from collections import Counter
counter=Counter(['red','blue','red','green','blue','blue'])
print(counter['blue'])
print(counter['green'])
print(dict(counter))

# 최대공약수 최소공배수
import math
def lcm(a,b):
    return a*b//math.gcd(a,b)
a=21
b=14

print(math.gcd(21,14)) # 최대공약수
print(lcm(21,14)) # 최소공배수

# 소수 1보다 큰 자연수 중에서 1과 자기자신을 제외한 자연수로는 나누어 떨어지지 않는 자연수 
def is_prime_number(x):
    for i in range(2,x):
        if x%i==0:
            return False
    return True

print(is_prime_number(4))
print(is_prime_number(7))

import math
def is_prime_number(x):
    for i in range(math.sqrt(x)+1):
        if x%i==0:
            return False
    return True

print(is_prime_number(4))
print(is_prime_number(7))

# 다수의 소수 판별 에라토스테네스의 체 알고리즘 
import math
n=1000
array=[True for i in range(n+1)]
for i in range(2,int(math,sqrt(n))+1):
    if array[i]==True
    j=2
    while i*j<=n:
        array[i*j]=False
        j+=1
    
for i in range(2,n+1):
    if array[i]:
        print(i,end=' ')

# 시간복잡도 o(nloglogn) 메모리는 많이 필요 

# 이진 탐색 알고리즘
# 순차탐색 디이터를 찾기 위해 앞에서부터 데이터를 하나씩 확인
# 이진탐색 탐색 범위를 절반씩 좁혀가며 데이터를 탐색
# 시간복잡도 o(logn)

def binary_search(array,target,start,end):
    if start>end:
        return None
    mid =(start+end)//2
    if array[mid]==target:
        return mid
    elif array[mid]>target:
        return binary_search(array,target,start,mid-1)
    else:
        return binary_search(array,target,start,mid+1,end)

n,target=list(map(int,input().split()))
array=list(map(int,input().split()))
result=binary_search(array,target,0,n-1)
if result==None:
    print('원소가 존재하지 않습니다')
else:
    print(result+1)

# bicect_left(a,x) 정렬된 순서를 유지하면서 배열 a에 x를 삽입할 가장 왼쪽 인덱스를 반환
# bisect_right(a,x) 정렬된 순서를 유지하면서 배열a에 x를 삽입할 가장 오른쪽 인덱스를 반환

from bisect import bisect_left,bisect_right
a=[1,2,4,4,8]
x=4
print(bisect_left(a,x))
print(bisect_left(a,x))

# 값이 특정 범위에 속하는 데이터 개수 구하기
from bisect import bisect_left, bisect_right
def count_by_range(a,left_value, right_value):
    right_index=bisect_right(a,right_value)
    left_index=bisect_left(a,left_value)
    return right_index-left_index

a=[1,2,3,3,3,3,4,4,8,9]
print(count_by_range(a,4,4))
print(count_by_range(a,-1,3))

# 파라메트릭 서치 최적화문제를 결정 예 아니오 
# 떡볶이 떡 만들기 적절한 높이를 찾을 때까지 이진탐색을 수행 높이 h를 반복조정 조건의 만족 여부에 따라서 탐색 범위를 좁혀서 해결

n,m=list(int,input().split()))
array=list(map(int,input().spllit()))
start=0
end=max(array)
result=0
while(start<=end):
    total=0
    mid=(start+end)//2
    for x in array:
        if x > mid:
            total+=x-mid
    if total<m:
        end=mid-1
    else:
        result=mid
        start=mid+1
print(result)

# 정렬된 배열에서 특정 수의 개수 구하기
from bisect import bisect_left,bisect_right
def count_by_range(array,left_value,right_value):
    right_index=bisect_right(array,right_value)
    left_index=bisect_left(array,left_value)
    return right_index-left_index

n,x=map(int,input().split()))
array=list(map(int,inpu(0.split())))
count=count_by_range(array,x,y)

if count==0:
    print(-1)
else:
    print(count)

# 동적 계획법
# 다이나믹 프로그래밍 메모리를 적절히 사용하여 수행 시간 효율성을 비약적으로 향상
# 이미 계산된 결과는 별도의 메모리 영역에 저장하여 다시 계산하지 않음
# 탑다운(하향식)  바텀업(상향식,전형적인형태) 바텀업 방식의 결과 저장용 리스트 dp테이블
# 동적(dynamic) 프로그램이 실행되는 도중에 시행에 필요한 메모리를 할당하는 기법
# 최적부분구조      큰문제를 작은 문제로 나눌수 잇다 작은문제의 답을 모아서 해결
# 중복되는 부분문제 동일한 작은 문제를 반복적으로 해결

# 피보나치 수열 
def fibo(x):
    if x==1 or x==2:
        return 1
    return fibo(x-1)+fibo(x-2)
print(fibo(4))

# 메모이제이션 한번계산한 결과를 메모리 공간에 미모 값을 기록해놓는다는 점에서 캐싱이라 표현

# 피보나치 수열 탑다운 
d=[0]*100
def fibo(x):
    if x==1 or x==2:
        return 1
    if d[x]!=0:
        return d[x]
    d[x]=fibo(x-1)+fibo(x-2)
    return d[x]

print(fibo(99))

# 피보나치 수열 바텀업
d=[0]*100
d[1]=1
d[2]=1
n=99
for i in range(3,n+1):
    d[i]=d[i-1]+d[i-2]
print(d[n])

# 피보나치 수열 메모이제이션 동작분석
d=[0]*100
def fubi(x):
    print('f('+str(x)+')',end=' ')
    if x==1 or x ==2:
        return 1
    if d[x]!=0:
        return d[x]
    d[x]= fibo(x-1)+fibo(x-2)
    return d[x]
fibo(6)

# 다이나믹 프로그래밍 최적 부분구조 부분 문제 중복
# 분할정복 최적부분구조 반복계산x
# 가장 먼저 그리디, 구현, 완전탐색 등 다른 알고리즘으로 풀이 방법이 떠오르지 않는다면 다이나믹 프로그래밍을 고려 
# 일단 재귀함수로 비효율적인 완전탐색 프로그램을 작성한뒤 탑다운 작은 문제에서 구한 답이 큰 문제에서 그대로 사용될 수 있으면 코드를 개선하는 방법을 사용

# 개미전사
n=int(input())
array=list(map(int,input().split()))
d=[0]*100
d[0]=array[0]
d[1]=max(array[0],array[1])
for i in range(2,n):
    d[i]=max(d[i-1],d[i-2]+array[i])
print(d[n-1])

x=int(input())
d=[0]*30001
for i in range(2,x+1):
    d[i]=d[i-1]+1
    if i%2==0:
        d[i]=min(d[i],d[i//2]+1)
    if i%3==0:
        d[i]=min(d[i],d[i//5]+1)
    if i%5==0:
        d[i]=min(d[i],d[i//5]+1)
print(d[x])

# 효율적인 화폐구성
n,m=map(int,input().split())
array=[]
for i in range(n):
    array.append(int(input()))
d=[10001]*(m+1)
d[0]=0
for i in range(n):
    for j in range(array[i],m+1):
        if d[j-array[i]]!=10001:
            d[j]=min(d[j],d[j-array[i]]+1)
if d[m]==10001:
    print(-1)
else:
    print(d[m])

# 금광
for tc in range(int(input())):
    n,m=map(int,input().split())
    array=list(map(int,input().split()))
    dp=[]
    index=0
    for i in range(n):
        dp.append(array[index:index+m])
        index+=m
    for j in range(1,m):
        for i in range(n):
            if i==0: 
                left_up=0
            else:
                left_up=dp[i-1][j-1]
            if i==n-1:
                left_down=0
            else:
                left_down=dp[i+1][j-1]
            left=dp[i][j-1]
            dp[i][j]=dp[i][j]+max(left_up,left_down,left)
    result=0
    for i in range(n):
        result=max(result,dp[i][m-1])
    print(result)

# 병사 배치하기
n=int(input())
array=list(mpa(int,input().split()))
array.reverse()
dp=[1]*n
for i in range(1,n):
    for j in range(0,i):
        if array[j]<array[i]:
            dp[i]=max(dp[i],dp[j]+1)
print(n-max(dp))

# 그리디 알고리즘 현재 상황에서 지금 당장 좋은 것만 고르는 방법 최적의 해가 되는 상황에서 이를 추론할 수 있어야 풀리도록 출제
# 거스름돈
n=1260
count=0
array=[500,100,50,10]
for coin in array:
    count+=n//coin
    n%=coin
print(count)

# 1이 될때까지
n,k = map(int,input().split())
result=0
while True:
    target=(n//k)*kresult +=(n-target)
    n=target
    if n<k:
        break
    result+=1
    n//=k
result+=(n-1)
print(result)

# 곱하기 혹은 더하기
data=input()
result=int(data[0])
for i in range(1,len(data)):
    num=int(data[i])
    if num <=1 or result<=1:
        result+=num
    else:
        result*=num

print(result)

#모험가 길드
n=int(input())
data=list(map(int,input().split()))
data.sort()
result=0
count=0
for i in data:
    count+=1
    if count>=i:
        result+=1
        count=0
print(result)

# 구현
# 풀이를 떠올리는 것은 쉽지만 소스코드로 옮기기 어려운 문제
# 알고리즘 간단 코드가 김
# 실수연산 소수점자리까지 출력
# 문자열 끊어처리
# 적절한 라이브러리

# 행열(matrix)
for i in range(5):
    for j in range(5):
        print('(',i,',',j,',end='' )
    print()

# 동,북,서,남
dx=[0,-1,0,1]
dy=[1,0,-1,0]
x,y=2,2
for i in range(4):
    nx=x+dx[i]
    ny=y+dy[i]
    print(nx,ny)

# 상하좌우
n=int(input())
x,y=1,1
plans=input().split()
dx=[0,0,-1,1]
dy=[-1,1,0,0]
move_types=['L','R','U','D']
for plan in plans:
    for i in range(len(move_types)):
        if plan==move_types[i]:
            nx=x+dx[i]
            ny=y+dy[i]
    if nx<1 or ny<1 or nx>n or ny>n:
        continue
    x,y=nx,no_type_check
print(x,y)

# 시각 
h=int(input())
count=0
for i in range(h+1):
    for j in range(60):
        if '3'in str(i)+str(j)+str(k):
            count+=1
print(count)

# 왕실의 나이트
input_data=input()
row=int(input_data[1])
column=int(ord(input_data[0]))-int(ord('a'))+1
steps=[(-2,-1),(-1,-2),(1,-2),(2,-1),(2,1),(1,2),(-1,2),(-2,1)]
result=0
for step in steps:
    next_row=row+step[0]
    next_column=column+step[1]
    if next_row>=1 and next_row<=8 and next_column>=1 and next_column<=8:
        result+=1
print(result)

# 문자재정렬
data=input()
result=[]
value=0
for x in data:
    if x.isalpha():
        else:
            value+=int(x)
ruesult.sort()
if value!=0:
    result.append(str(value))
print(''.join(result))

# 투 포인터 알고리즘 리스트에 순차적으로 접근해야할 때 두개의 점 위치를 기록하면서 처리 시작점과 끝점

# 특정한 합을 가지는 부분 연속 수열 찾기
n=5
m=5
data=[1,2,3,4,5]
count=0
interval_sum=0
end=0
for start in range(n):
    while interval_sum<m and end<n:
        interval_sum+=data[end]
        end+=1
    if interval_sum==m:
        count+=1
    interval_sum-=data[start]
print(count)

# 구간 합 빠르게 계산하기
# 접두사합 배열의 맨 앞부터 특정 위치까지 합을 미리 구해 놓은것
n=5
data=[10,20,30,40,50]
sum_value=0
prefix_sum=[0]
for i in data:
    sum_value+=i
    prefix_sum.append(sum_value)
left=3
right=4
print(prefix_sum[right]-prefix_sum[left-1])
