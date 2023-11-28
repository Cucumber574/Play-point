import os #для очистки экрана
from random import randint
''' 
игрок:
    имя
    здоровье
    деньги
    опыт
    уровень

сражается
играет в кости
покупает в лавке
'''

def start_game():
    ''' создает игрока и отправляет к камню'''
    player_name = input("введите имя игрока: ")
    player_hp = 100
    player_money = 10
    player_xp = 0
    player_level = 1
    player_potions = 0
    show_hero(player_name, player_hp, player_money, player_xp, player_level, player_potions)
    visit_rock(player_name, player_hp, player_money, player_xp, player_level, player_potions)

def show_hero(name, hp, money, xp, level, potions):
    ''' Выводит на экране инфо персонажа'''
    print('имя:', name)
    print('здоровье:', hp)
    print('деньги:', money)
    print('опыт:', xp)
    print('уровень:', level)
    print('зелья:', potions)


def visit_rock(player_name, player_hp, player_money, player_xp, player_level, player_potions):
    ''' камень: выбор дороги '''
    os.system('cls') #чистит экран
    print(player_name, 'приехал к камню')
    print(' 1 - Поехать на арену')
    print(' 2 - Отправится в таверну')
    print(' 3 - Заглянуть в лавку')
    print(' 0 - Уйти из игры')
    option = input('Введите номер варианта: ')
    if option == '1': 
        print('Уехал на арену')
    elif option == '2': 
        visit_tavern(player_name, player_hp, player_money, player_xp, player_level, player_potions)
    elif option == '3': 
        print('Уехал в лавку')
    elif option == '0': 
        print('Вышел из игры')
    else:
        visit_rock(player_name, player_hp, player_money, player_xp, player_level, player_potions)

def visit_tavern(player_name, player_hp, player_money, player_xp, player_level, player_potions):
    ''' Можно играть в кости или уйти к камню'''
    os.system('cls')
    print(player_name, 'приехал в таверну')
    print('1 - Сыграть в кости')
    print('2 - Вернуться к камню')
    print('0 - Выйти из игры')
    option = input('Введите номер варианта: ')
    if option == '1': 
        play_dice(player_name, player_hp, player_money, player_xp, player_level, player_potions)
    elif option == '2': 
        visit_rock(player_name, player_hp, player_money, player_xp, player_level, player_potions)
    elif option == '0': 
        print('Вышел из игры')
    else:
        visit_tavern(player_name, player_hp, player_money, player_xp, player_level, player_potions)


def play_dice(player_name, player_hp, player_money, player_xp, player_level, player_potions):
    os.system('cls')
    show_hero(player_name, player_hp, player_money, player_xp, player_level, player_potions)
    bet = int(input('Введите ставку: '))
    if not player_money:
        print('У', player_name, 'нету денег')
        input('Нажмите ENTER чтобы продолжить')
        visit_tavern(player_name, player_hp, player_money, player_xp, player_level, player_potions)
    elif bet < 1:
        print('Ставка должна быть больше нуля')
        input('Нажмите ENTER чтобы продолжить')
        play_dice(player_name, player_hp, player_money, player_xp, player_level, player_potions)
    elif bet > player_money:
        print('Недостатчно денег')
        input('Нажмите ENTER чтобы продолжить')
        play_dice(player_name, player_hp, player_money, player_xp, player_level, player_potions)

    player_score = randint(2, 12)
    tavern_score = randint(2, 12)
    print('Игрок выбросил', player_score)
    print('Трактирщик выбросил', tavern_score)
    if player_score > tavern_score:
        player_money += bet
        print(player_name, 'выиграл', bet, 'монет')   
    elif player_score < tavern_score:
        player_money -= bet
        print(player_name, 'проиграл', bet, 'монет')
    else player_score = tavern_score:
        print('Ничья')


def buy(player_name, player_hp, player_money, player_xp, player_level, player_potions):
    ''' Можно купить что то или уйти к камню'''
    os.system('cls')
    print(player_name, 'приехал в лавку')
    print('1 - Купить предмет')
    print('2 - Вернуться к камню')
    print('0 - Выйти из игры')
    option = input('Введите номер варианта: ')


def buy(player_name, player_hp, player_money, player_xp, player_level, player_potions):
    os.system('cls')
    show_hero(player_name, player_hp, player_money, player_xp, player_level, player_potions)
    bet = int(input('Что хотите купить: '))
    if not player_money:
        print('У', player_name, 'нету денег')
        input('Нажмите ENTER чтобы продолжить')
        visit_tavern(player_name, player_hp, player_money, player_xp, player_level, player_potions)
    elif bet > player_money:
        print('Недостатчно денег')
        input('Нажмите ENTER чтобы продолжить')
        buy(player_name, player_hp, player_money, player_xp, player_level, player_potions)


start_game()