# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет
date = int(input("вляется ли этот день выходным "))
if date >= 1 and date <= 5:
    print("Нет")
else:
    print("Да")
