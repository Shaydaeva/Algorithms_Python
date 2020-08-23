"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный
и отсортированный массивы.

Пример:
Введите число элементов: 5
Исходный - [46.11436617832828, 41.62921998361278, 18.45859540989644, 12.128870723745806, 8.025098788570562]
Отсортированный - [8.025098788570562, 12.128870723745806, 18.45859540989644, 41.62921998361278, 46.11436617832828]
"""
import random
import timeit


def merge_sort(lst_obj):
    if len(lst_obj) > 1:
        center = len(lst_obj) // 2
        left = lst_obj[:center]
        right = lst_obj[center:]

        merge_sort(left)
        merge_sort(right)

        # перестали делить
        # выполняем слияние
        i, j, k = 0, 0, 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                lst_obj[k] = left[i]
                i += 1
            else:
                lst_obj[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            lst_obj[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            lst_obj[k] = right[j]
            j += 1
            k += 1
        return lst_obj


def merge(lst_l, lst_r):
    res = []
    i = 0
    j = 0
    while i < len(lst_l) and j < len(lst_r):
        if lst_l[i] <= lst_r[j]:
            res.append(lst_l[i])
            i += 1
        else:
            res.append(lst_r[j])
            j += 1
    res += lst_l[i:] + lst_r[j:]
    return res


def merge_sort_2(lst_obj):
    if len(lst_obj) <= 1:
        return lst_obj
    else:
        left = lst_obj[:len(lst_obj) // 2]
        right = lst_obj[len(lst_obj) // 2:]
    return merge(merge_sort_2(left), merge_sort_2(right))


orig_list_10 = [random.random()*50 for _ in range(10)]
print(orig_list_10)
print(merge_sort(orig_list_10[:]))
orig_list_100 = [random.random()*50 for _ in range(100)]
orig_list_1000 = [random.random()*50 for _ in range(1000)]

# замеры
print(timeit.timeit("merge_sort(orig_list_10[:])",
                    setup="from __main__ import merge_sort, orig_list_10", number=10),
      timeit.timeit("merge_sort(orig_list_100[:])",
                    setup="from __main__ import merge_sort, orig_list_100", number=10),
      timeit.timeit("merge_sort(orig_list_1000[:])",
                    setup="from __main__ import merge_sort, orig_list_1000", number=10),
      sep='\n'
      )


# замеры
print(timeit.timeit("merge_sort_2(orig_list_10[:])",
                    setup="from __main__ import merge_sort_2, orig_list_10", number=10),
      timeit.timeit("merge_sort_2(orig_list_100[:])",
                    setup="from __main__ import merge_sort_2, orig_list_100", number=10),
      timeit.timeit("merge_sort_2(orig_list_1000[:])",
                    setup="from __main__ import merge_sort_2, orig_list_1000", number=10),
      sep='\n'
      )

'''
На 100 итераций:
0.003494900000000002
0.0630936
0.8332347
0.00364780000000009
0.05418689999999993
0.7504312

На 10 итераций, как в первом задании, разница хороша)
И с ростом массива всё эффективней работает
[28.50769763025886, 24.112102284443175, 19.039047466015063,
 20.281562125672824, 28.328642165307315, 16.675499098377582,
 39.79649605144953, 28.280270690610305, 32.46249640927848,
 21.643050678774866]
[16.675499098377582, 19.039047466015063, 20.281562125672824,
 21.643050678774866, 24.112102284443175, 28.280270690610305,
 28.328642165307315, 28.50769763025886, 32.46249640927848,
 39.79649605144953]
 
0.00038900000000000046
0.006562399999999996
0.0842656
0.00032740000000000546
0.005762600000000007
0.07791559999999997

Не стала делать пользовательский ввод, чтобы проверить
на нужном мне количестве чисел
'''
