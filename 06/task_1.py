"""
Задание 1.
Выполните профилирование памяти в скриптах
Проанализировать результат и определить программы с
наиболее эффективным использованием памяти.

Примечание: Для анализа возьмите любые 1-3 ваших программы или несколько
вариантов кода для одной и той же задачи. Можно взять задачи с курса Основ или с текущего курса Алгоритмов

Результаты анализа вставьте в виде комментариев к коду.
Также укажите в комментариях версию Python и разрядность вашей ОС.

ВНИМАНИЕ: ЗАДАНИЯ, В КОТОРЫХ БУДУТ ГОЛЫЕ ЦИФРЫ ЗАМЕРОВ (БЕЗ АНАЛИТИКИ)
БУДУТ ПРИНИМАТЬСЯ С ОЦЕНКОЙ УДОВЛЕТВОРИТЕЛЬНО
"""
from memory_profiler import profile
from pympler import asizeof
from random import randint


@profile
def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


nums=list(range(1000000))

func_1(nums)


lst = [randint(0, 100) for i in range(20)]


# Линейная
@profile
def search_min_1(lst):
    min_obj = lst[0]

    for i in range(len(lst) - 1):
        if min_obj > lst[i+1]:
            min_obj = lst[i+1]
    return min_obj


(search_min_1(lst))
print(asizeof.asizeof(lst))
print(asizeof.asizeof(search_min_1(lst)))

'''
Line #    Mem usage    Increment   Line Contents
================================================
    32     32.6 MiB     32.6 MiB   @profile
    33                             def func_1(nums):
    34     32.6 MiB      0.0 MiB       new_arr = []
    35     42.1 MiB      0.0 MiB       for i in range(len(nums)):
    36     42.1 MiB      0.1 MiB           if nums[i] % 2 == 0:
    37     42.1 MiB      0.2 MiB               new_arr.append(i)
    38     42.1 MiB      0.0 MiB       return new_arr
    
Line #    Mem usage    Increment   Line Contents
================================================
    14     22.2 MiB     22.2 MiB   @profile
    15                             def search_min_1(lst):
    16     22.2 MiB      0.0 MiB       min_obj = lst[0]
    17                             
    18     22.2 MiB      0.0 MiB       for i in range(len(lst) - 1):
    19     22.2 MiB      0.0 MiB           if min_obj > lst[i+1]:
    20     22.2 MiB      0.0 MiB               min_obj = lst[i+1]
    21     22.2 MiB      0.0 MiB       return min_obj


432

Line #    Mem usage    Increment   Line Contents
================================================
    14     22.2 MiB     22.2 MiB   @profile
    15                             def search_min_1(lst):
    16     22.2 MiB      0.0 MiB       min_obj = lst[0]
    17                             
    18     22.2 MiB      0.0 MiB       for i in range(len(lst) - 1):
    19     22.2 MiB      0.0 MiB           if min_obj > lst[i+1]:
    20     22.2 MiB      0.0 MiB               min_obj = lst[i+1]
    21     22.2 MiB      0.0 MiB       return min_obj


16
'''

'''
По итогам проверки кодов не получилось выявить значительных затрат
памяти, возможно где-то можно было применить значительное увеличение
данных сохраняемых в переменных и обрабатываемых в дальнейшем.
Обработку больших объемов информации лучше производить с 
помощью специализированных инструментов, как например numpy,
неиспользуемые данные можно удалять.
Использовании объекта генератора так же не забивает память, но
его реализация возможна не везде.
'''