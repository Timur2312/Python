import random
from unittest import result
# def select(f,col):
#     return [f(x) for x in col]

# def where (f,col):
#     return [x for x in col if f(x)]

# data = '1 2 3 5 8 15 23 38'.split()

# res = select(int,data)
# res = where(lambda x: not x%2, res)
# res = select(lambda x:(x,x**2),res)
# print(res)

# Задайте списко из нескольких чисел. Напишите программу, которая найдет сумму элементов списка, стоящих на нечентной позиции 

# num = random.randint(7,17)
# list_of_numbers = []
# sum = 0
# for i in range(num):
#     list_of_numbers.append(random.randint(1,100))
#     if i % 2 !=0:
#         sum +=list_of_numbers[i]
# print(list_of_numbers)
# print(sum)

# Напишите программу, которая найдет произведение пар чисел списка.
# Парой считается первый и последний элемент, второй и предпоследний.

# def creat_list(num):
#     list_of_numbers = []
#     for i in range(num):
#         list_of_numbers.append(random.randint(1, 11))
#     print(list_of_numbers)
#     return list_of_numbers

# def calc_list(list_of_numbers):
#     if len(list_of_numbers)%2==0:
#         for i in range(len(list_of_numbers)//2):
#             print(list_of_numbers[i]*list_of_numbers[-i-1])
#     else :
#         for i in range(len(list_of_numbers)//2+1):
#             print(list_of_numbers[i]*list_of_numbers[-i-1])

# num = random.randint(7, 10)
# list_of_numbers = creat_list(num)
# calc_list(list_of_numbers)

# напишите программу, кторая будет преобразовывать десятичное число в двоичное.

# def dec_to_bin(num):
#     result = ""
#     while num >0:
#         result = str(num % 2) + result
#         num//=2
#     return result

# x = random.randint(1,100)
# print(x)
# bin_num=dec_to_bin(x)
# print(bin_num)