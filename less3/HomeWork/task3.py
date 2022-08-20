# 3) Вводим строчку и выводим разницу между количеством букв в верхнем и нижнем регистре.
text = input("Введите текс ")
lower_case = 0
upper_case = 0
for i in text:
    if i == i.lower():
        lower_case += 1
    if i == i.upper():
        upper_case += 1
print(f"Количество букв в нижнем регистре = {lower_case}")
print(f"Количество букв в верзнем регистре = {upper_case}")
print(f"Разница между ними = {lower_case - upper_case}")
