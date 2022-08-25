# ДЗ 1
# 1) Создать список случайных чисел от - 10, до 10 на num * 2 элементов. num вводим с клавиатуры.
#     2) Вывести все числа меньше 0 и делящиеся на 3
#     3) Сказать кол-во элементов 5 и 3
#     4) Вывести разницу между кол-вом максимальных и минимальных значений
#     5) Сделать копию списка. Равзернуть и упорядочить список список
#     6) Удалить половину элементов списка
#     7) Очистить список



from audioop import reverse
from hashlib import new
import random


def is_int():
	while(True):
		number = input("Введите количество элементов в массиве (цифрой) ")
		if number.isdigit() == True:
			return int(number)
		else:
			print("Ошибка вы ввели не число")
def get_list(number):
	list_numbers = [number]
	for i in range(1,number):
		list_numbers.append(random.randint(-10, 11))
	return list_numbers


amount_of_elemenets = is_int()*2
list_of_numbers = get_list(amount_of_elemenets)
print(list_of_numbers)
print("Все числа меньше числа 0 и делящиеся на 3")
for i in list_of_numbers:  # Вывести все числа меньше 0 и делящиеся на 3
	if i < 0 or i % 3 == 0:
		print(i, end=" ")
print()
five = 0
three = 0
for i in list_of_numbers:
	if i == 5:five+=1
	if i == 3: three+=1
print(f"Количество элементов со значением 5 = {five}")
print(f"Количество элементов со значением 3 = {three}")
print(f"Разница между кол-вом максимальных и минимальных значений {max(list_of_numbers) - min(list_of_numbers)}")

new_list = list_of_numbers.copy()
print(new_list)

new_list.reverse()
print(new_list)


if len(list_of_numbers) % 2 == 0:
	del list_of_numbers[:len(list_of_numbers)//2]
	print(list_of_numbers)
else :
	del list_of_numbers[:len(list_of_numbers)//2+1]
	print(list_of_numbers)

list_of_numbers.clear()

print(list_of_numbers)
