# Методы строк
# str1 = "Текст"
# print(str1.lower())
# print(str1.count(какой элмент нужно посчитать)) Делает подсчет сколько элементов в строке
# print(str1.replace(старое значение , новое значение )) Заменяет значения
# print(str1.isalpha()) Проверят состоит ли текст только букв (вовзрашает булева значение)
# print(str1.isdighit()) Проверят состоит ли текст только цифр (вовзрашает булева значение)


# Вводим строчку и удаляем из неё все буквы 'a'
# str1 = input("Введите текст ")
# print(str1.replace("а", ""))


# Вводим строчку делим её пополам и переставляем их местами.
# # Выводим на экран результат

# str1 = input()
# str2 = len(str1)
# if str2 % 2 == 0:
#     str3 = str1[str2//2:] + str1[0: str2//2]
#     print(str3)
# else:
#     str3 = str1[str2//2 + 1:] + str1[0: str2//2 + 1]
#     print(str3)

# 3) Вводим строчку и выводим на экран: 1 - 3 символ, 2 - каждый 4 символ, 3 - все символы в обратном порядке

# str1 = input()
# print(str1[0:4])
# str1 = str1[5::4]
# print(str1)
# str1 = str1[::-1]
# print(str1)
# if str1 % 4 == 0:
#     str1 = str1[]
#  4) Вводим строчку и выводим  количество букв в верхнем регистре.

# str1 = input()
# count = 0
# for i in str1:
#     if i == i.upper():
#         count += 1
# print(count)