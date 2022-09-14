# 1.1. Напишите программу вычисления арифметического выражения заданного строкой. Используйте операции +,-,/,*. приоритет операций стандартный.

# *Пример:* 
# 2+2 => 4; 
# 1+2*3 => 7; 
# 1-2*3 => -5;


expression = input('Что вычислить?')
print(eval(expression))



# Тут я пытался описать сам, но у меня не получилось, можете кинуть как это должно выглядить 


# def two_numbers(len):
#     if expression[1] == "*":
#         result = int(expression[0])*int(expression[2])
#         return result
#     elif expression[1] == "/":
#         result = int(expression[0])/int(expression[2])
#     elif expression[1] == "-":
#        result = int(expression[0])-int(expression[2])
#        return result
#     elif expression[1] == "+":
#         result = int(expression[0])+int(expression[2])
#         return result 


# expression =(input()).split()
# if expression[1]=="*" or expression[1]=="/":
#     if expression[1]=="*":
#         result = int(expression[0])*int(expression[2])
#     if expression[1] == "/":
#         result = int(expression[0])/int(expression[2])
# result+=int(expression[4])

# if expression[1] == "+" or expression[1] == "-":
#     if expression[1] == "+":
#         result = int(expression[0])+int(expression[2])
#     if expression[1] == "/":
#         result = int(expression[0])/int(expression[2])
# result += int(expression[4])



# print(result)


