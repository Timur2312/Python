# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
import random
candy = 100
player_one = 1
count_candy_player_one=0
player_two = 2
count_candy_player_two = 0
def take_candy():
    player = 0
    while True:
        take = int(input())
        if candy >= take:
            if take <= 28:
                player += take
                return player
            else:
                print("Вы взяли слишком много конфет, возьмите не больше чем 28")
        else: 
            print(f"На столе меньше конфет чем вы пытаетесь взять, на столе {candy} конфет")
            
def bot_candy():
    player = 0
    while True:
        take = random.randint(1,28)
        if candy >= take:
            if take <= 28:
                player += take
                return player
            else:
                print()
        else: 
            take = random.randint(1, candy)

def who_first(player_one , player_two):
    players = [1,2]
    result = random.choice(players)
    if result == 1:
        return player_one
    else:
        return player_two

step = who_first(player_one, player_two)
while candy > 0:
    if step == 1:
        print("Ход первого игрока, возьми конфеты но не больше 28 ")
        player_one = take_candy()
        candy -= player_one
        count_candy_player_one += player_one
        step = 2
    else:
        player_two = bot_candy()
        print(f"Бот взял {player_two} конфет")
        candy -= player_two
        count_candy_player_two += player_two
        step = 1
        
if count_candy_player_one > count_candy_player_two:
    print(
        f"Победил первый игрок\n Конфеты первого игрока: {count_candy_player_one} \n Конфеты Бота : {count_candy_player_two}")
elif count_candy_player_one < count_candy_player_two:
    print(
        f"Победил Второй игрок\n Конфеты первого игрока: {count_candy_player_one} \n Конфеты Бота : {count_candy_player_two}")
else:
    print(
        f"Ничья\n Конфеты первого игрока: {count_candy_player_one} \n Конфеты Бота : {count_candy_player_two}")





