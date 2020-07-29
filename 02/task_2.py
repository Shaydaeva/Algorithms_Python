"""
2.	Посчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, то у него 3 четные цифры
(4, 6 и 0) и 2 нечетные (3 и 5).

Подсказка:
На каждом шаге вам нужно 'доставать' из числа очередную цифру
и смотреть является ли она четной или нечетной. При этом увеличиваем соответствующий счетчик
Пока все числа не извлечены рекурсивные вызовы продолжаем
Условие завершения рекурсии - все числа извлечены

Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7

Пример:
Введите число: 123
Количество четных и нечетных цифр в числе равно: (1, 2)
"""


#  user_input == 0  # базовое условие
def parity_recursion(user_input, even, odd):
    """Рекурсия"""
    if user_input == 0:
        return f'Количество четных цифр - {even}, нечетных {odd}'
    else:
        user_input, remainder = user_input // 10, user_input % 10
        if remainder % 2 == 0:
            even += 1
        else:
            odd += 1
        return parity_recursion(user_input, even, odd)


user_input = input('Введите число: ')
even = 0  # четные
odd = 0  # нечетные

#  блок проверки входных данных
try:
    user_input = int(user_input)
except ValueError:
    print('Необходимо ввести натуральное число')
else:
    if user_input < 1:
        print('Необходимо ввести натуральное число')
    else:
        print(parity_recursion(user_input, even, odd))

# --------------------------------------------------------------------


def parity_cycle():
    """Цикл"""
    user_input = input('Введите число: ')
    even = 0  # четные
    odd = 0  # нечетные

    #  блок проверки входных данных
    try:
        user_input = int(user_input)
    except ValueError:
        print('Необходимо ввести натуральное число')
    else:
        if user_input < 1:
            print('Необходимо ввести натуральное число')

    while user_input != 0:
        user_input, remainder = user_input // 10, user_input % 10
        if remainder % 2 == 0:
            even += 1
        else:
            odd += 1
    print(f'Количество четных цифр - {even}, нечетных {odd}')


parity_cycle()

# --------------------------------------------------------------------


"""
В первом варианте данной фунции, если на вход придет число начинающееся с нуля, например 0123, то функция int()
автоматически преобразует его в 123, мне кажется в нашем случае это не очень правильно, поэтому немного изменила
решение, чтобы обрабатывать и такой вариант
"""


def parity_recursion_2(user_input, even, odd):
    """Рекурсия"""
    if len(user_input) == 0:
        return f'Количество четных цифр - {even}, нечетных {odd}'
    else:
        user_input, remainder = user_input[:-1], int(user_input.pop())
        if remainder % 2 == 0:
            even += 1
        else:
            odd += 1
        return parity_recursion_2(user_input, even, odd)


user_input = input('Введите число: ')
even = 0  # четные
odd = 0  # нечетные

#  блок проверки входных данных
try:
    check = int(user_input)
except ValueError:
    print('Необходимо ввести натуральное число')
else:
    if check < 1:
        print('Необходимо ввести натуральное число')
    else:
        print(parity_recursion_2(list(user_input), even, odd))
