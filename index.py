#Задача 1 булен
x=True
y=False
print(type(x))
print(type(y))
#Задача 2
age = 22
print(age>6)
print(age>=6)
print(age<=6)
print(age==6)
print(age!=6)
print(age>6)
#Задача 3
password = "liga"
print(password==input("Введите пароль"))
#Задача 4
password = "liga"
age = 21
print(password==(input("Введите пароль")) or age>6)
print(password==(input("Введите пароль")) and age>6)
print(password==(input("Введите пароль")) or not age>6)
#Задача 5
age = int(input("Введите возраст"))
if age>6 and age<18:
    print("Вы вероятно ходите в школу")
#Задача 6
x = int(input("Введите число 1"))
y = int(input("Введите число 2"))
if x>y:
    print("первое число больше")
#Задача 7
x = input("Введите слово")
if x=="ручка" or x=="чернила":
    print("Да ручка")
#Задача 8
age = int(input("Введите возраст"))
if age>6 and age<18:
    print("Вы вероятно ходите в школу")
if age<6:
    print("Вы Малыш")
#Задача 9
x = int(input("Введите число 1"))
y = int(input("Введите число 2"))
if x>6 and y>6:
    print("o6a числа больше 6")
