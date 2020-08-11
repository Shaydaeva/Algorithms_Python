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

# t1 = Timer("func_1(a)", "from __main__ import func_1\na = [i for i in range(1000)]")
# print(t1.timeit(number=1000))
#
stat_1 = repeat(st, setup, number=1000)
print(f'var 1 {sum(stat_1) / len(stat_1)}')
# print(timeit("func_1(a)", "from __main__ import func_1\na = [i for i in range(1000)]", number=1000))
print('var 1 ', timeit(st, setup, number=1000))

# ------------------------------------------------------------------


def func_2(nums):
    new_arr = []
    for i in nums:
        if i % 2 == 0:
            new_arr.append(nums[i])
    return new_arr


setup = "nums=list(range(1000))"

st = '''new_arr = []
for i in nums:
    if i % 2 == 0:
        new_arr.append(nums[i])
'''

# t2 = Timer("func_2(a)", "from __main__ import func_2\na = list(range(1000))")
# print(t2.timeit(number=1000))
#
stat_2 = repeat(st, setup, number=1000)
print(f'my var 2 {sum(stat_2) / len(stat_2)}')
# print(timeit("func_2(a)", "from __main__ import func_2\na = list(range(1000))", number=1000))
print('my var 2 ', timeit(st, setup, number=1000))


def func_3(nums):
    return [nums[i] for i in nums if i % 2 == 0]


st = '[nums[i] for i in nums if i % 2 == 0]'

setup = "nums=list(range(1000))"

stat_3 = repeat(st, setup, number=1000)
print(f'list comp var 3 {sum(stat_3) / len(stat_3)}')
print('list comp var 3 ', timeit(st, setup, number=1000))


def func_4(nums):
    return [i for i, el in enumerate(nums) if el % 2 == 0]


st = '[i for i, el in enumerate(nums) if el % 2 == 0]'

setup = "nums=list(range(1000))"

stat_4 = repeat(st, setup, number=1000)
print(f'enum var 4 {sum(stat_4) / len(stat_4)}')
print('enum var 4', timeit(st, setup, number=1000))

'''
Померила разные варианты, в итоге list comprehension самый быстрый получился,
а при использовании list comprehension с enumerate скорость сопоставима с
моим вариантом, когда обращение идет не по индексу, а к самим элементам

var 1 0.23716620000000002
var 1  0.22468120000000003
my var 2 0.16891628
my var 2  0.15600309999999995
list comp var 3 0.14387870000000005
list comp var 3  0.1363588
enum var 4 0.16962659999999996
enum var 4 0.16509079999999976
'''
