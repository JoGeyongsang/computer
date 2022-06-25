name="광재"
print("%s는 나의 친구입니다."% name)

animal_0="cat"
animal_1="dog"
animal_2="fox"

print("Animal:{0}".format(animal_0))
print("Animal:{0},{1},{2}".format(animal_0,animal_1,animal_2))

yourname=input("당신의 이름은? ")
print("당신은 {}이군요.".format(yourname))

num=input("숫자를 입력하세요: ")
print("당신이 입력한 숫자는 {}입니다.".format(num))

def my_func():
  print("my first function!")
  print("this is a function.")

my_func()

def my_friend(friendname):
  print("{}는 나의 친구입니다.".format(friendname))

my_friend("철수")
my_friend("영미")

def print_name(name):
  if bool(name):
    print("입력된 이름:",name)
  else:
    print("입력된 이름이 없습니다.")

print_name("james")
print_name("")