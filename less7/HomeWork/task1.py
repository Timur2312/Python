# Cоздать телефонный справочник используя файлы, модули и исключения

def check_number(number):
    try:
     number = int(number)
     return  True
    except:
       return False

count = 0
while count < 2:
    name = input("Введите сове имя: ") 
    number = input("Введите совой номер: ")
    answer = None
    if check_number(number):
        with open('names.txt','a') as file: 
            file.write(f"Имя: {name}\n")
            file.write(f"Номер: {number}\n")
            file.write("-----------------------\n")
            count +=1
    else:
       print("Вы ввели не корректный номер телефона.")
       answer = input("Продолжим ввод ? ")
       if answer.lower() == "да":
          continue
       else:
        break





