"""
1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран
исходный и отсортированный массивы. Сортировка должна быть реализована в
виде функции. Обязательно доработайте алгоритм (сделайте его умнее).

Идея доработки: если за проход по списку не совершается ни одной сортировки,
то завершение
Обязательно сделайте замеры времени обеих реализаций
и обосновать дала ли оптимизация эффективность

Подсказка: обратите внимание, сортируем не по возрастанию, как в примере,
а по убыванию
"""
import timeit
import random


def bubble_sort(lst_obj):
    """Сортировка пузырьком по убыванию"""
    n = 1
    while n < len(lst_obj):
        for i in range(len(lst_obj)-n):
            if lst_obj[i] < lst_obj[i+1]:
                lst_obj[i], lst_obj[i+1] = lst_obj[i+1], lst_obj[i]
        n += 1
    return lst_obj


def better_bubble_sort(lst_obj):
    is_shift = 1
    n = 1
    while is_shift:
        is_shift = 0
        for i in range(len(lst_obj)-n):
            if lst_obj[i] < lst_obj[i+1]:
                lst_obj[i], lst_obj[i+1] = lst_obj[i+1], lst_obj[i]
                is_shift = 1
        n += 1
    return lst_obj


orig_list_10 = [random.randint(-100, 100) for _ in range(10)]
print('Стандартная: ', orig_list_10, bubble_sort(orig_list_10[:]), sep='\n')
print('Доработанная: ', orig_list_10, better_bubble_sort(orig_list_10[:]), sep='\n')
orig_list_100 = [random.randint(-100, 100) for _ in range(100)]
orig_list_1000 = [random.randint(-100, 100) for _ in range(1000)]

# замеры 10
print(timeit.timeit("bubble_sort(orig_list_10[:])",
                    setup="from __main__ import bubble_sort, orig_list_10", number=10),
      timeit.timeit("bubble_sort(orig_list_100[:])",
                    setup="from __main__ import bubble_sort, orig_list_100", number=10),
      timeit.timeit("bubble_sort(orig_list_1000[:])",
                    setup="from __main__ import bubble_sort, orig_list_1000", number=10),
      sep='\n')

print(timeit.timeit("better_bubble_sort(orig_list_10[:])",
                    setup="from __main__ import better_bubble_sort, orig_list_10", number=10),
      timeit.timeit("better_bubble_sort(orig_list_100[:])",
                    setup="from __main__ import better_bubble_sort, orig_list_100", number=10),
      timeit.timeit("better_bubble_sort(orig_list_1000[:])",
                    setup="from __main__ import better_bubble_sort, orig_list_1000", number=10),
      sep='\n')

'''
Стандартная: 
[54, 18, -27, 69, 20, -30, 98, -38, -92, -44]
[98, 69, 54, 20, 18, -27, -30, -38, -44, -92]
Доработанная: 
[54, 18, -27, 69, 20, -30, 98, -38, -92, -44]
[98, 69, 54, 20, 18, -27, -30, -38, -44, -92]
0.00023470000000000435
0.0210505
2.2759473
0.00021310000000029916
0.021045599999999887
2.2523033000000003

После оптимизации время не изменилось, оптимизация не имеет смысла
'''