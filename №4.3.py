from random import randint


def pl_input():
    while True:
        res = input('Ваш ход: ')
        if res in ['1', '2', '3']:
            return int(res)
        else:
            print('Введите верные данные (число от 1 до 3)')


def win_strg(stones):
    flag = 0
    while stones > 0:
        pl_turn = pl_input()
        stones -= pl_turn
        print('Остатолось:', stones)
        if flag == 0:
            answ = input('Вам не победить. Желаете продолжить? (Да/Нет) ')
            if answ.upper() == 'ДА':
                flag = 1
            else:
                return '\nВы проиграли'
        bot_turn = 4 - pl_turn
        stones -= bot_turn
        print('Ход бота:', bot_turn)
        print('Остатолось:', stones, '\n')
    return 'Вы проиграли'


def lose_strg(stones):
    flag = 0
    while stones > 0:
        bot_turn = randint(1, 3)
        stones -= bot_turn
        print('Ход бота:', bot_turn)
        print('Остатолось:', stones, '\n')
        flag = 1
        if stones > 0:
            pl_turn = pl_input()
            stones -= pl_turn
            print('Остатолось:', stones)
            flag = 0
    if flag == 0:
        return '\nВы победили!'
    else:
        return 'Вы проиграли'


def main(stones):
    print('Добро пожаловать!\n')
    print('Перед вами лежит кучка камней')
    print('Вы можете убирать из нее от одного до трех камней')
    print('Побеждает тот, кто забирает последний камень')
    print('Вероятность победы бота: 75%\n')
    print('Начальное число камней:', stones)
    if stones % 4 == 0:
        return win_strg(stones)
    else:
        pl_turn = pl_input()
        stones -= pl_turn
        print('Остатолось:', stones)
        if stones % 4 == 0:
            return lose_strg(stones)
        else:
            value = 0
            bot_turn = 0
            while value < stones:
                if value % 4 == 0:
                    bot_turn = stones - value
                    value += 1
                else:
                    value += 1
            stones -= bot_turn
            print('Ход бота:', bot_turn)
            print('Остатолось:', stones, '\n')
            return win_strg(stones)


print(main(randint(4, 30)))
