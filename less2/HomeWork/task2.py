# 2) Вводим с клавиатуры целое число X
#     Далее вводим Х целых чисел.
#     Необходимо вывести на экран максимальное и второе максимальное число из введенных чисел.

a = int(input("Введите число "))
b = int(input("Введите число "))
c = int(input("Введите число "))
max = a
second = 0
if a > max:
    max = a
if b > max:
    max = b
if c > max:
    max = c
print(max)
if a > b and a < max:
    second = a
if a > c and a < max:
    seocnd = a
if b > a and b < max:
    second = b
if b > c and b < max:
    second = b
if c > a and c < max:
    second = c
if c > b and c < max:
    second = c
print(second)
