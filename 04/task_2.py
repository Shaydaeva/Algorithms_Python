"""
Задание 2.

Приведен код, который формирует из введенного числа
обратное по порядку входящих в него цифр.
Задача решена через рекурсию

Сделайте замеры времени выполнения кода с помощью модуля timeit

Попробуйте оптимизировать код, чтобы снизить время выполнения
Проведите повторные замеры

Подсказка: примените мемоизацию

Добавьте аналитику: что вы сделали и почему

------------------------------------------
Не совсем поняла, приведенная функция добавляет 0 в конец нашего обратного числа,
исправила для себя. Или я что-то не так поняла?

"""
from timeit import timeit
from random import randint


def recursive_reverse(number):
    if number == 0:
        # return str(number % 10)
        return ''
    return f'{str(number % 10)}{recursive_reverse(number // 10)}'


num_100 = randint(10000, 1000000)
num_1000 = randint(1000000, 1000000000)
num_10000 = randint(100000000, 1000000000000)

print('')
print(timeit('recursive_reverse(num_100)',
             'from __main__ import recursive_reverse, num_100',
             number=1000))
print(timeit('recursive_reverse(num_1000)',
             'from __main__ import recursive_reverse, num_1000',
             number=1000))
print(timeit('recursive_reverse(num_10000)',
             'from __main__ import recursive_reverse, num_10000',
             number=1000))


def memo(f):
    cache = {}

    def decorate(number):
        if number in cache:
            return cache[number]
        else:
            cache[number] = f(number)
            return cache[number]
    return decorate


@memo
def recursive_reverse_2(number):
    if number == 0:
        # return str(number % 10)
        return ''
    return f'{str(number % 10)}{recursive_reverse(number // 10)}'


num_100 = randint(10000, 1000000)
num_1000 = randint(1000000, 1000000000)
num_10000 = randint(100000000, 1000000000000)

print(recursive_reverse_2(123456789))
print(timeit('recursive_reverse_2(num_100)',
             'from __main__ import recursive_reverse_2, num_100',
             number=1000))
print(timeit('recursive_reverse_2(num_1000)',
             'from __main__ import recursive_reverse_2, num_1000',
             number=1000))
print(timeit('recursive_reverse_2(num_10000)',
             'from __main__ import recursive_reverse_2, num_10000',
             number=1000))

'''
Попробовала код, что писали на уроке.
Пробовала написать что-то подобное, когда выпоняла домашку, но не получалось.

0.006744
0.009142599999999994
0.011423699999999995
987654321
0.00046960000000000057
0.0004965999999999998
0.0003803000000000001
'''
