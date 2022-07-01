# 2557
print("Hello World!")

# 2884
a,b=map(int,input().split())
if b<45:
  if(a !=0):
    print(a-1,60-45+b)
  else:
    print(23-a, 60-45+b)
elif b>=45:
  print(a, b-45)

# 2525
h,m=map(int,input().split())
time=int(input())

h=h+(time//60)
m=m+(time%60)
if m>=60:
  h=h+1
  m=m-60
if h>=24:
  h=h-24
print(h,m)

# 2480
a,b,c=map(int,input().split())
if a==b==c :
  print(10000+a*1000)

elif a==c or a==b:
  print(1000+a*100)

elif b==c:
  print(1000+b*100)

else:
  print(max(a,b,c)*100)

# 2739번
x=int(input())
for y in range(1,10):
  print(x,"*",y,"=",x*y)

# 10950번
a=int(input())
for i in range (1,a+1):
  c,b=map(int,input().split())
  d=c+b
  print(d)

# 8393번
a=int(input())
i=0
for b in range(1,a+1):
  i=i+b
print(i)

# 2741
a=int(input())
for i in range(1,a+1):
  print(i)

# 2742
a=int(input())
for i in range(a,0,-1):
  print(i)

# 11021
n=int(input())
for i in range(1,n+1):
  a,b=map(int,input().split())
  print("Case #"+str(i)+":",a+b)

# 10871
a,b=map(int,input().split())
c=list(map(int,input().split()))
for i in range(a):
  if c[i]< b :
    print(c[i],end=" ")

# 10952
while True:
  a,b=map(int,input().split())
  if a+b!=0:
    print(a+b)
    continue
  else:
    break

# 10951
while True:
  try:
    a,b=map(int,input().split())
    print(a+b)
  except:
    break

# 1110
N = int(input())                             
n = -1                                      
t = 0                                        
while n != N:                                
	if n == -1: n = N                        
	n = (n//10 + n%10)%10 + (n%10)*10        
	t += 1                                   
print(t)        

# 10818
numArr = []
a = int(input())
b = list(map(int, input().split()))
for i in range(a) :
  numArr.append(b[i])
numMax = max(numArr)
numMin = min(numArr)
print(numMin,numMax)

# 2562
a=[]

for i in range(9):
    a.append(int(input()))
    
print(max(a))
print(a.index(max(a))+1)

# 2577
a=int(input())
b=int(input())
c=int(input())

d=a*b*c

numlist=list(str(d))
numlist1=[0]*10
for i in range(0,10):
  for n in numlist:
    if str(i)== n:
      numlist1[i]+=1
for k in numlist1:
  print(k)

# 3052
arr = []
for i in range(10):
    n = int(input())
    arr.append(n % 42)
arr = set(arr)
print(len(arr))

# 1546
a = int(input())
num = list(map(int, input().split()))
maxNum = max(num)

for i in range(len(num)) :
  num[i] = num[i]/maxNum*100

avgNum = sum(num)/len(num)
print(avgNum)