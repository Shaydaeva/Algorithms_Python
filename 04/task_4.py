"""
Задание 4.

Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.

Сделайте профилировку каждого алгоритма через timeit

Попытайтесь написать третью версию, которая будет самой быстрой.
Сделайте замеры и опишите, получилось ли у вас ускорить задачу.
-------------------------------------------------

Первая функция показалась и без улучшений вполне красивой)
Судя по замерам, использование множества для прохождения в цикле
все же немного ускоряет задачу..
"""
from timeit import timeit
from collections import Counter

array = [1, 3, 1, 3, 4, 5, 1]


def func_1():
    m = 0
    num = 0
    for i in array:
        count = array.count(i)
        if count > m:
            m = count
            num = i
    return f'Чаще всего встречается число {num}, ' \
           f'оно появилось в массиве {m} раз(а)'


def func_2():
    new_array = []
    for el in array:
        count2 = array.count(el)
        new_array.append(count2)

    max_2 = max(new_array)
    elem = array[new_array.index(max_2)]
    return f'Чаще всего встречается число {elem}, ' \
           f'оно появилось в массиве {max_2} раз(а)'


def func_3():
    m = 0
    num = 0
    for i in set(array):
        count = array.count(i)
        if count > m:
            m = count
            num = i
    return f'Чаще всего встречается число {num}, ' \
           f'оно появилось в массиве {m} раз(а)'


def func_4():
    m = max(array, key=array.count)
    return f'Чаще всего встречается число {m}, ' \
           f'оно появилось в массиве {array.count(m)} раз(а)'


print(func_1())
print(func_2())
print(func_3())
print(func_4())
print(timeit("func_1()", "from __main__ import func_1", number=100000))
print(timeit("func_2()", "from __main__ import func_2", number=100000))
print(timeit("func_3()", "from __main__ import func_3", number=100000))
print(timeit("func_4()", "from __main__ import func_4", number=100000))

'''
В сравнении с лаконичным и красивым func_4, он однако отрабатывает с той же
скоростью, по крайней мере на моей машине, что и первый вариант, и с множеством
все равно быстрее

0.35172200000000003
0.4781286
0.2897278
0.3555474999999999
'''
