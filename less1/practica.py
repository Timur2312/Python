
# Выводит запрошенное число и предыдушие и следующие число
#a = int(input())
# print(f"{a-1}{a}{a+1}")

# Выводит первую и вторую цифру числа
#a = input("Введите число ")
#print(f" десятков {a[0]} единиц {a[1]}")
# Второй вариант
#a = int(input("Введите число "))
#print(f" Десятков - {a // 10}  Единиц - {a %10}")

# Программа зарпшивет возраст и если возраст меньше 18 то выводит доступ запрещен
#age = int(input("Введите свой возврат "))
# if age < 18:
#    print("Доступ запрещен")
# else:
#    print("Доступ разрешен")

# Вводим с клавитуры размеры сторон треугольника и говорим какой
# он обычныйБ равнобедренный или равносторонний

#x1= int(input("Введите первую сторону треугольника"))
#x2= int(input("Введите первую сторону треугольника"))
#x3= int(input("Введите первую сторону треугольника"))
#if x1==x2 and x2==x3: print("равносторонний")
# elif x1 == x2 or x2== x3 or x1==x3: print("Равнобедренный")
# else: print("обычный")

# 3) Напшите программу где вводим три числа а потом ввыодим сумму только положительных чисел

#a = int(input("Введите число"))
#b = int(input("Введите число"))
#c = int(input("Введите число"))
#sum = 0
# if a >= 0:
#    sum = sum + a
# if b >0 :
#    sum = sum + b
# if c >=0:
#    sum = sum + c
# print(sum)

# Программа которая по ввёденому вострасу пользователя сообщает в какой онв группе

#age = int(input("Введите ваш возраст "))
#if age < 13: print ("детство")

# elif age <= 24 : print("Молодость")
# elif age <=59 : print("Зрелость")
# else: print("Старость")


# *Вводим с клавиатуры два целых числа X и Y ( X <  Y).
#Необходимо найти целое число из отрезка [X; Y] с максимальной суммой делителей.
#x = int(input("Введите X"))
#y = int(input("Введите Y"))



# Вводим с клавы число х - целое, а затем вводим х разных целых чисел.
# Нужно вывести на экран самое большое и второе по величине число из введенных.

a = int(input("Введите число "))
b = int(input("Введите число "))
c = int(input("Введите число "))
max = 0
second = 0
if max < b:
    max = b
if max < c:
    max = c
print(max)
if a < b : second = b
if a > b : second = a
if b < c : second = b
if b > c : second = c
print(second)
