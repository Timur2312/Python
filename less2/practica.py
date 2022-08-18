# №1
# Вводим число n с клавиатуры и слово и вывести данное словов в столбик N раз

# numbre = int(input("Введите число скольок раз нужно повторить слово "))
# word = input("Введите слово ")

# for i in range(numbre):
#     print(word)

# № 2 В первой задаче выводим слово N раз в одной строке и N Столбцов

# numbre = int(input("Введите число скольок раз нужно повторить слово "))
# word = input("Введите слово ")
# for row in range(numbre):
#     print(word * numbre)

# № 3 Вводим число N с клавиатуры и выводим таблицу умножения от 1 до N

# numbre = int(input("До кого числа выводить таблицу умножения "))
# for row in range(1, numbre+1):
#     for column in range(1, 11):
#         print(f"{row} * {column} = {row * column}")
#     print()

# № 4 Вводим целые числа X и Y. Необходимов вывести на экран все числа делящиеся на 3 между X и Y

# x = int(input("Введите X "))
# y = int(input("Введите Y "))
# for i in range(x, y+1):
#     if i % 3 == 0:
#         print(i)

# while
# № 5 Вводим с клавиатуры числа делящиеся на 3. Программа будет работать до тех пор пока не введем число не делящее на 3

# number = int(input("Введите число "))
# while (number % 3 == 0):
#     number = int(input("Введите число "))

# № 6 Вводим с клавиатуры целое число. Выводим его цифры в обратном порядке.
# number = int(input("Введите число "))
# while number > 0:
#     print(number % 10)
#     number = number // 10

# № 7 Вводим число N с клавиатуры. N > 2. Необходимо вывести на экран наиминьший делитель
while True:
    number = int(input("Введите число больше 2 "))
    if number > 2:
        break
    else:
        print("Вы ввелие не верное число")
# while i <= number:
#     i = i + 1
#     if number % i == 0:
#         print(i)
#         break
    # Второй способ
for i in range(2, number+1):
    if number % i == 0:
        print(i)
        break
