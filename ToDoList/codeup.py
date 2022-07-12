# 6001 
print("Hello")

# 6002
print("Hello World")

# 6003
print("Hello")
print("World")

# 6004
print("'Hello'")

# 6005
print('"Hello World"')

# 6006
print("\"!@#$%^&*()'")

# 6007
print("\"C:\\Download\\'hello'.py\"")

# 6008
print("print(\"Hello\\nWorld\")")

# 6009
a=input()
print(a)

# 6010
a=int(input())
print(a)

# 6011
f=float(input())
print(f)

# 6012
a=int(input())
b=int(input())
print(a)
print(b)

# 6013
a=input()
b=input()
print(b)
print(a)

# 6014
f=float(input())
print(f)
print(f)
print(f)

# 6015
a,b=map(int,input().split())
print(a)
print(b)

# 6016
a,b=input().split()
print(b,a)

# 6017
a=input()
print(a,a,a)

# 6018
a, b = input().split(':')
print(a, b, sep=':')

# 6019
a,b,c=input().split('.')
print(c,b,a,sep="-")

# 6020
a,b=input().split('-')
print(a,b,sep='')

# 6021
a=input()
print(a[0])
print(a[1])
print(a[2])
print(a[3])
print(a[4])

# 6022
a=input()
print(a[0:2],a[2:4],a[4:6])

#6023
a,b,c=input().split(':')
print(b)

# 6024
a,b=input().split()W
print(a+b)

# 6025
a,b=map(int,input().split())
print(a+b)

# 6026
a=float(input())
b=float(input())
print(a+b)

# 6027
a = input()
n = int(a)          
print('%x'% n)

# 6028
a = input()
n = int(a)          
print('%X'% n)

# 6029
a = input()
n = int(a, 16)
print('%o' % n)

# 6030
a = ord(input())
print(a)

# 6031
a = int(input())
print(chr(a)) 

# 6032
a=int(input())
print(-a)

# 6033
a = input()
b = ord(a)
print(chr(b+1))

# 6034
a,b=map(int,input().split())
print(a-b)

# 6035
a,b=map(float,input().split())
print(a*b)

# 6036
a,b=input().split()
print(a*int(b))

# 6037
a=int(input())
b=input()
print(b*int(a))

# 6038
a,b=map(int,input().split())
print(a**b)

# 6039
a,b=map(float,input().split())
print(a**b)

# 6040
a,b=map(int,input().split())
print(a//b)

# 6041
a,b=map(int,input().split())
print(a%b)

# 6042
a=float(input())
print(format(a,".2f"))

# 6043
a,b=map(float,input().split())
print(format(a/b,".3f"))

# 6044
a,b=map(int,input().split())
print(a+b)
print(a-b)
print(a*b)
print(a//b)
print(a%b)
print(format(a/b,".2f"))

# 6045
a,b,c=map(int,input().split())
print(a+b+c,format((a+b+c)/3,".2f"))

# 6048
a,b=map(int,input().split())
if a<b:
  print(True)
else:
  print(False)

# 6049
a,b=map(int,input().split())
if a==b:
  print(True)
else:
  print(False)

# 6050
a,b=map(int,input().split())
if a<=b:
  print(True)
else:
  print(False)

# 6051
a,b=map(int,input().split())
if a==b:
  print(False)
else:
  print(True)

# 6052
a=int(input())
if a==0:
  print(False)
else:
  print(True)

# 6053
a=bool(int(input()))
if a==False:
  print(True)
else:
  print(False)

# 6054
a,b=map(int,input().split())
if (bool(a)==True) and (bool(b)==True):
  print(True)
else:
  print(False)

# 6055
a,b=map(int,input().split())
if (bool(a)==True) or (bool(b)==True):
  print(True)
else:
  print(False)

# 6056
a,b=map(int,input().split())
if (bool(a)) != (bool(b)):
  print(True)
else:
  print(False)

# 6057
a,b=map(int,input().split())
if (bool(a)) == (bool(b)):
  print(True)
else:
  print(False)

# 6058
a,b=map(int,input().split())
if (bool(a)==False) and (bool(b)==False):
  print(True)
else:
  print(False)

# 6059
a = int(input())
print(~a)

# 6060
a, b = input().split()
print(int(a)&int(b))

# 6061
a,b = input().split()
print(int(a)|int(b))

# 6062
a,b = input().split()
print(int(a)^int(b))

# 6063
a,b=map(int,input().split())
if a>b:
  print(a)
else:
  print(b)

# 6064
a,b,c=map(int,input().split())
print(min(a,b,c))

# 6065
a,b,c=map(int,input().split())
if a%2==0:
  print(a)
if b%2==0:
  print(b)
if c%2==0:
  print(c)

# 6066
a,b,c=map(int,input().split())
if a%2==0:
  print('even')
else:
  print('odd')
if b%2==0:
  print('even')
else:
  print('odd')
if c%2==0:
  print('even')
else:
  print('odd')

# 6067
a=int(input())
if a<0:
  if a%2==0:
    print('A')
  else:
    print('B')
else:
  if a%2==0:
    print('C')
  else:
    print('D')

# 6068
a=int(input())
if a>=90:
  print('A')
elif a>=70:
  print('B')
elif a>=40:
  print('C')
else:
  print('D')

# 6069
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

# 6070
a=int(input())
if (a>=3) and (a<=5):
  print('spring')
elif (a>=6) and (a<=8):
  print('summer')
elif (a>=9) and (a<=11):
  print('fall')
else:
  print('winter')  

# 6086
a=int(input())
b=0
c=0
while True:
  b+=1
  c=c+b
  if c>=a:
    break
print(c)