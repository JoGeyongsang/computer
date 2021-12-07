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