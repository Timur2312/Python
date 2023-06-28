import clases


# Запись в файл нового работника 
def add_Employee (number,name,job_title):
    with open('Employees.txt','a') as file:
         pass
    with open('Employees.txt','r') as file:
        check_Number(number)
        str_number = f"Номер: {number}"
        if check_Employee(str_number,file):
            with open('Employees.txt','a') as file:
                file.write(f"Номер: {number}\n Имя: {name}\n Должность: {job_title}\n")
        else:
            print("Такой сотрудник уже есть в базе")

# Проверка на наличие сотрудника
def check_Employee (str,file):
    with open('Employees.txt','r') as file:
        check = True
        for line in file.readlines():
            if str in line:
                check = False 
                return check
        return check
    
# Проверка номера телефона
def check_Number(number):
    try:
        int(number)
    except:
        print(f"Вы ввели не корректное число {number}")
            
# Поиск сотрудника
def search_Employee(name):
    with open('Employees.txt','r') as file:
         for line in file.readlines():
             if name in line:
                 print(line)
                 print()
               
                 