# 2) Вводим строчку и выводим на экран:
#     * общее количество символов в строке;
#     * каждый чётный символ,
#     * все символы в обратном порядке
text = input("Введите текст ")
print(f"Общее количество символов в строке {len(text)}")
print(f"Каждый чётный символ {text[2::2]}")
print(f"Все символы в обратном порядке {text[::-1]}")
