"""
4.	Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.

Пример:
Введите количество элементов: 3
Количество элементов - 3, их сумма - 0.75

Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
"""


def sum_elem_recursion(n, sum, num):
    """Рекурсия"""
    if n == 0:
        return sum
    else:
        sum += num
        num /= -2
        n -= 1
        return sum_elem_recursion(n, sum, num)


def sum_elem_cycle(n, sum, num):
    """Цикл"""
    for i in range(n):
        sum += num
        num /= -2
    return sum

sum = 0
num = 1
n = input('Введите количество элементов: ')

#  блок проверки входных данных
try:
    n = int(n)
except ValueError:
    print('Необходимо ввести количество элементов')
else:
    if n < 1:
        print('Необходимо ввести количество элементов')
    else:
        print(sum_elem_recursion(n, sum, num))

