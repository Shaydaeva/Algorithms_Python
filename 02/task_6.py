"""
6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.

Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
"""

from random import randint


answer = randint(0, 100)
count = 10
print(answer)


def guess_number(ans, var):
    """Рекурсия"""
    if var == 0:
        print(f'К сожалению, попытки кончились\nБыло загадано {ans}')
    else:
        user_input = input('Угадайте число: ')
        if user_input.isdigit():
            user_input = int(user_input)
            var -= 1
            if ans == user_input:
                print(f'Поздравляю, Вы угадали!!!')
            elif answer > user_input:
                print(f'Больше (осталось {var} попыток)')
                return guess_number(ans, var)
            elif answer < user_input:
                print(f'Меньше (осталось {var} попыток)')
                return guess_number(ans, var)
        else:
            print('Загадано число, попробуйте угадать его, вводя числа')
            return guess_number(ans, var)


guess_number(answer, count)

# Цикл
while count >= 0:
    user_input = input('Угадайте число: ')
    if user_input.isdigit():
        user_input = int(user_input)
        count -= 1
        if user_input == answer:
            print('Поздравляю, Вы угадали!!!')
            break
        elif answer > user_input:
            print(f'Больше (осталось {count} попыток)')
        elif answer < user_input:
            print(f'Меньше (осталось {count} попыток)')
        if count == 0:
            print(f'К сожалению, попытки кончились\nБыло загадано {answer}')

    else:
        print('Загадано число, попробуйте угадать его, вводя числа')

