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