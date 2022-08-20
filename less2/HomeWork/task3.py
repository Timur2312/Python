# 3) Вводим с клавиатуры целое число - это зарплата.
#     Нужно вывести в консоль - Минимальное кол-во  купюр, которыми можно выдать ЗП.
#     И сколько, и каких бухгалтер выдаст 25 рублевых купюр,  10 рублевых, 5 рублевых и 1 рублевых


salary, total25, total10, total5, total1, = int(
    input("Введите свою зарплату ")), 0, 0, 0, 0

while salary >= 25:
    salary -= 25
    total25 += 1
while salary >= 10:
    salary -= 10
    total10 += 1
while salary >= 5:
    salary -= 5
    total5 += 1
while salary >= 1:
    salary -= 1
    total1 += 1

print(f'{total25}  {total10}  {total5}  {total1}')
