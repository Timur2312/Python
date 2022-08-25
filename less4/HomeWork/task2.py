# ДЗ 2
# Сгенерировать список на num элементов от 150 до 200. num вводим с клавиатуры.
# Мы вводим с клавиатуры какое-то число в этом диапазоне(от 150 до 200).
# Это построение по росту в строю. Необходимо поставить в строй введеный лемент
# Например: сгенерировались 163, 175, 169, 200
# Вбили с клавиатуры 180
# Вы второй в строю. И вывести список.
from audioop import reverse
from hashlib import new
import random

def is_int():
	while(True):
		number = input()
		if number.isdigit() == True:
			return int(number)
		else:
			print("Ошибка вы ввели не число")
def get_list(number):
    list_numbers = []
    for i in range(0,number):
        list_numbers.append(random.randint(150,200))
    return list_numbers


print("Введите количество элементов в массиве(цифрой)")
amount_of_elemenets = is_int()
list_numbers = get_list(amount_of_elemenets)

list_numbers.sort()
print(list_numbers)

print("Введите свой рост от 150 до 200 ")
while(True):
    add_new_element = is_int()
    if add_new_element >= 150 or add_new_element <=200:
        list_numbers.insert(0, add_new_element)
        break
    else:print("Ошибка вы ввели не не верное число")

list_numbers.sort()
print (list_numbers)

print(f"Вы {list_numbers.index(add_new_element)} в строю ")
