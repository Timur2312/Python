# 1) Вводим с клавиатуры целое число X и У.
# Выводим на экран количество чисел между Х и У, которые делятся на 2 и 3


x = int(input("Введите X "))
y = int(input("Введите Y "))
count = 0
for i in range(x, y+1):
    if i % 2 == 0 or i % 3 == 0:
        count += 1
print(count)
