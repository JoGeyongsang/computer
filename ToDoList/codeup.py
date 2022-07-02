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