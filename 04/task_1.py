"""
Задание 1.

Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива

Сделайте замеры времени выполнения кода с помощью модуля timeit

Попробуйте оптимизировать код, чтобы снизить время выполнения
Проведите повторные замеры

Добавьте аналитику: что вы сделали и почему

-------------------------------------------------------
Поменяла обращение по индексу к элементу на сам элемент,
что немного добавило скорости
"""

from timeit import Timer, repeat, default_timer, timeit


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


setup = "nums=list(range(1000))"

st = '''new_arr = []
for i in range(len(nums)):
    if nums[i] % 2 == 0:
        new_arr.append(i)
'''

t1 = Timer("func_1(a)", "from __main__ import func_1\na = [i for i in range(1000)]")
print(t1.timeit(number=1000))

print(repeat(st, setup, default_timer, 3, 1000))
print(timeit("func_1(a)", "from __main__ import func_1\na = [i for i in range(1000)]", number=1000))
print(timeit(st, setup, number=1000))

# ------------------------------------------------------------------


def func_2(nums):
    new_arr = []
    for i in nums:
        if i % 2 == 0:
            new_arr.append(nums[i])
    return new_arr


st = '''new_arr = []
for i in nums:
    if i % 2 == 0:
        new_arr.append(nums[i])
'''

t2 = Timer("func_2(a)", "from __main__ import func_2\na = list(range(1000))")
print(t2.timeit(number=1000))

print(repeat(st, setup, default_timer, 3, 1000))
print(timeit("func_2(a)", "from __main__ import func_2\na = list(range(1000))", number=1000))
print(timeit(st, setup, number=1000))
