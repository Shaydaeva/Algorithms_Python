"""
Задание 3.

Для этой задачи:
1) придумайте 1-3 решения (желательно хотя бы два)
2) оцените сложность каждого решения в нотации О-большое
3) сделайте вывод, какое решение эффективнее и почему

Примечание:
Без выполнения пунктов 2 и 3 задание считается нерешенным. Пункты 2 и 3 можно выполнить
через строки документации в самом коде.
Если у вас возникают сложности, постарайтесь подумать как можно решить задачу,
а не писать "мы это не проходили)".
Алгоритмизатор должен развивать мышление, а это прежде всего практика.
А без столкновения со сложностями его не развить.


Сама задача:
Имеется хранилище с информацией о компаниях: название и годовая прибыль.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, реализовать словарь.
Реализуйте поиск трех компаний с наибольшей годовой прибылью.
Выведите результат.
"""

comp_info = {'comp1': 12345, 'comp2': 13627,
             'comp3': 15045, 'comp4': 12847,
             'comp5': 10944, 'comp6': 12385,
             'comp7': 19823, 'comp8': 19284,
             'comp9': 22345, 'comp10': 10045,
             'comp11': 12300}


def best_three(dict_comp):
    list_dict = list(dict_comp.items())
    list_dict.sort(key=lambda i: i[1], reverse=True)
    for i in range(3):
        print(list_dict[i][0], ' : ', list_dict[i][1])


best_three(comp_info)


def best_three_2(dict_comp):
    dict_for_sort = dict_comp.copy()
    list_for_sort = list(dict_for_sort.items())
    for _ in range(3):
        max_value = list_for_sort[0][1]
        key_max_value = 0
        for i in range(1, len(list_for_sort) - 1):
            if max_value < list_for_sort[i][1]:
                max_value = list_for_sort[i][1]
                key_max_value = i
        print(list_for_sort[key_max_value][0], ' : ', dict_for_sort.pop(list_for_sort[key_max_value][0]))
        del list_for_sort[key_max_value]


best_three_2(comp_info)

"""
Надо ещё подумать, может поинтересней вариант найду, 
но пока придумала только такие два.

best_three() - сложность линейно-логарифмическая O(n log n)
best_three_2() - сложность квадратичная O(n^2)

Первый вариант эффективней, так как используется меньше структур данных и
в целом меньше операций.
"""