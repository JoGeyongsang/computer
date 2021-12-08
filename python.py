# 파이썬 코드 작성 오답노트 

s =input()
print(s[0:2],s[2:4:1],s[4:6:1])

a = input()
b = input()
c = float(a)+float(b)
print(c)

a=ord(input())
print(chr(a+1))

a,b = input().split()
if (bool(int(a)) and (not bool(int(b)))) or ((not bool(int(a))) and bool(int(b))):
  print('True')
else:
  print('False')

a = 'a'
next = ord(a) + 1
print( chr(next) )

a,b = input().split()
if (bool(int(a)) and bool(int(b))) or (not bool(int(a)) and not bool(int(b))):
  print('True')
else:
  print('False')

#6022
s=input()
print(s[0:2],s[2:4],s[4:6])

#6023
a,b,c=input().split()
print(b)

#6024
w1,w2=input().split()

#6025
a,b=input().split()

#6027
a=input()
n=int(a)
print('%x'%n)



#6069
a=input()
if a=='A':
  print('best!!!')
elif a=='B':
  print('good!!')
elif a=='C':
  print('run!')
elif a=='D':
  print('slowly~')
else:
  print('what?')

#6070
a = int(input())
if a==12 or a<=2:
  print('winter')
elif a<=5:
  print('spring')
elif a<=8:
  print('summer')
elif a<=11:
  print('fall')

#6071 0입력될 때까지 무한 출력하기
a = int(input())
while a!=0:
  print(a)
  a=int(input())

#6072 정수 1개 입력받아 카운트다운 출력하기 
a=int(input())
while a!=0:
  print(a)
  a=a-1

#6074 문자 1개 입력받아 알파벳 출력하기
a= ord(input())
b= ord(a)
while b<=a:
  print(chr(b), end=' ')
  b+=1

#6075 정수 1개 입력받아 그 수까지 출력하기
a=int(input())
b=int(0)
while b<=a:
  print(b)
  b=b+1

#6076 정수 1개 입력받아 그 수까지 출력하기
a=int(input())
for i in range(n+1):
  print(i)

#6077 짝수  합 구하기
a=int(input())
b=0
for i in range(1,a+1):
  if i%2==0:
    b+=i
print(b)

#6078 원하는 문자가 입력될 때까지 반복 출력하기
a=ord('a')
q=ord('q')
while a!=q:
  a=ord(input())
  print(chr(a))

#6079 언제까지 더해야 할까?
sum=0
i=0
n=int(input())
while True:
  i=i+1
  sum=sum+i
  if(sum>=n):
    print(i)
    break

#6080 주사위 2개 던지기
a,b=input().split()
a=int(a)
b=int(b)
for i in range(1,a+1):
  for j in range(1,b+1):
    print(i,j)

#6081 16진수 구구단 출력하기
n=int(input(),16)
for j in range(1,16):
  print('%X*%X=%X'%(n,j,n*j))

#6082 369게임의 왕이 되자
n=int(input())
for i in range(1,n+1):
  if i%10==3 or i%10==6 or i%10==9:
    print('X',end=' ')
  else:
    print(i, end=' ')

#6083 빛 섞어 색 만들기
r,g,b=map(int,input().split())
n=0
for i in range(r):
  for j in range(g):
    for k in range(b):
      print(i,j,k)
      n=n+1
print(n)

#6084 소리 파일 저장용량 계산하기
h,b,c,s=map(int, input().split())
m=(h*b*c*s)/(8*1024*1024)
a=round(m,1)
x='MB'
print(a,x)

#6085 

n = int(input())
while True:
  if n>=0:
    print(n)
  else:break
  n=-1

#6092
n =int(input())
a=list(map(int,input().split()))
result=[0]*24
for i in range(n):
  result[a[i]]+=1
for i in range(1,len(result)):
  print(result[i],end=' ')

#6093
n=int(input())
a=list(map(int,input().split()))
result = [0]* 24
for i in range(n):
  a[i]=int(a[i])
for i in range(n-1,-1,-1):
  print(a[i],end=' ')

#6094
n=int(input())
a=list(map(int,input().split()))
mini=a[0]
maxi=a[0]
for i in a[1:]:
  if mini>i:
    mini=i
  if i>maxi:
    maxi=i
print(mini)
print(maxi)

n=int(input())
a=list(map(int,input().split()))
maxi=a[0]
for i in a[1:]:
  if i>maxi:
    maxi=i
print(maxi)
print(a.index(maxi)+1)


n=int(input())
for i in range(n,0,-1):
  print(i)

n =int(input())
while n:
  print(n)
  n-=1

n=int(input())
for ch in range(97,n+1):
  print(chr(ch),end=' ')

n=int(input())
for i in range(n+1):
  print(i,end=' ')

n=int(input())
total=0
for i range(1,n+1):
  total+=i
print(total)

n=int(input(),base=16)
for i in range(1,16):
  print(f'{n}*{i}={n*i}')

while True:
  ch =input()
  if ch !='q':
    print(ch)
  else:
    break

#구구단
n=int(input())
for x in range(2,10):
  for y in range(1,10):
    print(f'{x}*{y}={x*y}')

n=int(input())
for x in range(2,10):
  for y in range(1,10):
    print('{}*{}={}'.format(x,y,x*y))


for n in range(2,10):
  print(n, end=' ')
  print()

  for i in range(1,10):
    print(i,end=' ')
    print()

for n in range(2,10):
  print(n, end=' ')
  print()

  for i in range(1,10):
    print(i,end=' ')
  print()

#직사각형
for i in range(n):
  for j in range(n):
    print('*,end='')
  print()

#별찍기
n=int(input())
for x in range(1,n+1):
  for y in range(1,x+1):
    print('*',end='')
  print()

n=int(input())
for x in range(1,n+1):
  print(' '*(n-x),end='')
  print('*'*x)

n=int(input())
for x in range(n):
  for y in range(n-x):
    print(' ',end='')
  for z in range(x+1):
    print('*',end='')
  print()

n=int(input())
for x in range(n,0,-1):
  for y in range(x):
    print('*',end='')
  print()

n=int(input())
for x in range(n,0,-1):
  for y in range(n-x):
    print(' ',end='')
  for z in range(x):
    print('*',end='')
  print()

n=int(input())
for x in range(n,0,-1):
  for y in range(n-x):
    print(' ',end='')
  for z in range(x):
    print('*',end='')
  print()

n=int(input())
for x in range(1,n+1):
  for y in range(n-x):
    print(' ',end='')
  for z in range(2*x-1):
    print('*',end='')
  print()


a=int(input())
b=int(input())
c=int(input())
solve=list(map(int,str(a*b*c)))
ans=[0]*10
for i in solve:
  ans[i]+=1
print(*ans, sep='\n')

ans=[0]*42
for i in range(10):
  n=int(input())
  i=n%42
  ans[i]=1
print(sum(ans))