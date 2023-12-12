import os

inventory  = []
money = 100

while True:
    print('1 - купить зелье лечение за 10')
    print('2 - купить зелье копчение за 20')
    print('3 - продать')
    print('деньги:', money)
    print('инветарь:', inventory)

    option = input('Введите номер опции: ')
    if option == '1':
        money -= 10
        inventory.append('зелье лечение')
        print('Игрок купил зелья лечение')
    elif option == '2':
        money -= 20
        inventory.append('зелье копчение')
        print('Игрок купил зелья копчение')
    elif option == '3':
        print('Что хотите продать?')
        for item in inventory:
            print(idx, item)
            idx += 1
        option = input('Введите номер предмета который хотите продать')
        # проверка вменяемость опции
        inventory.pop(option)

    else:
        print('Эта неверная функция')

    input('ENTER - продолжить')