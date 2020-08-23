"""
3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на
две равные части: в одной находятся элементы, которые не меньше медианы,
в другой – не больше медианы.

Задачу можно решить без сортировки исходного
массива.

Но если это слишком сложно, то используйте метод сортировки,
который не рассматривался на уроках: Шелла, Гномья, ...

arr[m]
from statistics import median
"""
import random
import timeit
from statistics import median


def median_without_sort(lst_obj):
    left = []
    right = []
    med = 0
    a = sum(lst_obj)/len(lst_obj)

    for i in lst_obj:
        if i > a:
            right.append(i)
        elif i < a:
            left.append(i)
        else:
            med = i

    if med == 0:
        if len(left) > len(right):
            med = max(left)
        else:
            med = min(right)

    return med


def gnome_sort(lst_obj):
    i, j, size = 1, 2, len(lst_obj)
    while i < size:
        if lst_obj[i - 1] <= lst_obj[i]:
            i, j = j, j + 1
        else:
            lst_obj[i - 1], lst_obj[i] = lst_obj[i], lst_obj[i - 1]
            i -= 1
            if i == 0:
                i, j = j, j + 1
    return lst_obj


def median_gnome_sort(lst_obj):
    i, j, size = 1, 2, len(lst_obj)
    while i < size:
        if lst_obj[i - 1] <= lst_obj[i]:
            i, j = j, j + 1
        else:
            lst_obj[i - 1], lst_obj[i] = lst_obj[i], lst_obj[i - 1]
            i -= 1
            if i == 0:
                i, j = j, j + 1
    return lst_obj[len(lst_obj)//2]


m = int(input('Введите m: '))
orig_list = [random.randint(0, 100) for i in range(2*m+1)]
print(f'Массив: {orig_list}')

print(median(orig_list))
print(median_without_sort(orig_list))

print('Из модуля statistics:',
      timeit.timeit("median(orig_list[:])",
                    setup="from __main__ import orig_list, median", number=10000),
      'Моя без сортировки:',
      timeit.timeit("median_without_sort(orig_list[:])",
                    setup="from __main__ import orig_list, median_without_sort", number=10000),
      'С гномьей сортировкой:',
      timeit.timeit("median_gnome_sort(orig_list[:])",
                    setup="from __main__ import orig_list, median_gnome_sort", number=10000),
      sep='\n')

''' 
Введите m: 5
Массив: [42, 9, 76, 42, 80, 42, 1, 62, 59, 22, 50]
42
42
Из модуля statistics:
0.01249670000000025
Моя без сортировки:
0.045746799999999865
С гномьей сортировкой:
0.2310333

В моей функции используются некоторые встроенные функции, которые так же можно заменить на перебор,
время вполне приемлимое
С гномьей сортировкой время обработки увеличивается из-за наличия сортировки в целом
'''


