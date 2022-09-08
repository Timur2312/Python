# Дан список чисел. Создайте список, в который попадают числа, описываемые возрастающую последовательность.
# Порядок элементов менять нельзя.
# Пример:
# [1, 5, 2, 3, 4, 6, 1, 7] =>  [1, 7] 
import random
def get_list():
    list=[]
    for i in range(8):
        list.append(random.randint(1, 9))
    return list


list_of_numbers = get_list()
new_list=[]
print(list_of_numbers)
for i in range(len(list_of_numbers)-1):
    start = list_of_numbers[i]
    if start < list_of_numbers[i+1]:
        new_list.append(start)
        new_list.append(list_of_numbers[i+1])
    else:
        start = list_of_numbers[i]

print(new_list)