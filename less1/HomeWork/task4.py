# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

quarter = int(input("введите номер четверти "))

if quarter == 1:
    print("Возможный диапозон координат точке x = от 0 до бесконечности y = от 0 до бесконечности")
elif quarter == 2:
    print("Возможный диапозон координат точке x = от 0 до  - бесконечности y = от 0 до бесконечности")
elif quarter == 3:
    print("Возможный диапозон координат точке x = от 0 до  - бесконечности y = от 0 до  - бесконечности")
elif quarter == 4:
    print("Возможный диапозон координат точке x = от 0 до бесконечности y = от 0 до  - бесконечности")

else:
    print("нет такой четверти")
