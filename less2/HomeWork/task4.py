# 4) Вводим с клавиатуры многозначное число
# Необходимо узнать и сказать последовательность цифр этого числа при просмотре слева направо упорядочена по возрастанию или нет.
# Например 1579 - да ( 1 меньше 5, 5 меньше 7, а 7 меньше 9), 1427 - нет

number = int(input("Введите число "))
if number // 1000 < number // 100 % 10:
    number = number % 1000
if number // 100 < number // 10 % 10:
    number = number % 100
if number // 10 < number % 10:
    print("да")
else:
    print("нет")