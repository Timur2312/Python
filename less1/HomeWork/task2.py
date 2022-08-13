#Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
x = int(input("Введите X "))
y = int(input("Введите Y "))
z = int(input("Введите Z "))
left = not (x or y or z)
right = not x and not y and not z
result = left == right
if result == True : print("Истино")
else : print ("Лож")