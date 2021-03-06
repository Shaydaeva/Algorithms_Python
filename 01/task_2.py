"""
Задание 2.

Реализуйте два алгоритма.

Первый, в виде функции, должен обеспечивать поиск минимального значения для списка.
В основе алгоритма должно быть сравнение каждого числа со всеми другими элементами списка.
Сложность такого алгоритма: O(n^2) - квадратичная.

Второй, в виде функции, должен обеспечивать поиск минимального значения для списка.
Сложность такого алгоритма: O(n) - линейная.

Примечание:
Построить список можно через генератор списка.
Если у вас возникают сложности, постарайтесь подумать как можно решить задачу,
а не писать "мы это не проходили)".
Алгоритмизатор должен развивать мышление, а это прежде всего практика.
А без столкновения со сложностями его не развить.
"""

from random import randint

lst = [randint(0, 100) for i in range(20)]

# Линейная
def search_min_1(lst):
    min_obj = lst[0]

    for i in range(len(lst) - 1):
        if min_obj > lst[i+1]:
            min_obj = lst[i+1]
    return min_obj


print(search_min_1(lst))

# так же сложность будет линейной
min_num = min(lst)

print(lst)
print(min_num)

# n log n, если я правильно поняла
min_j = sorted(lst)[0]
print(min_j)


# Квадратичная
def min_num(lst):
    for i in range(0, len(lst) - 1):
        for j in range(i + 1, len(lst)):
            if lst[j] < lst[i]:
                lst[i], lst[j] = lst[j], lst[i]
    return lst[0]


print(min_num(lst))
print(lst)
