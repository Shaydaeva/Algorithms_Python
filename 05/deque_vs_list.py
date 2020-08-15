# from collections import deque
from timeit import timeit

print(' list', timeit('list(range(100000))', number=1000))
print('deque', timeit('deque(list(range(100000)))',
                      'from collections import deque',
                      number=1000))
print(' list.append', timeit('lst.append(9999)', 'lst = list(range(100000))', number=100000))
print('deque.append', timeit('my_deque.append(9999)',
                             'from collections import deque\nmy_deque = deque(list(range(100000)))',
                             number=100000))
print(' list.appendleft', timeit('lst.insert(0, 8888)', 'lst = list(range(100000))', number=100000))
print('deque.appendleft', timeit('my_deque.appendleft(8888)',
                                 'from collections import deque\nmy_deque = deque(list(range(100000)))',
                                 number=100000))
print(' list.extend', timeit('lst.extend(for_ext)', 'lst = list(range(100000))\n'
                                                    'for_ext = list(range(100, 200))', number=100000))
print('deque.extend', timeit('my_deque.extend(for_ext)',
                             'from collections import deque\n'
                             'my_deque = deque(list(range(100000)))\n'
                             'for_ext = list(range(100, 200))', number=100000))
print(' list.pop', timeit('lst.pop()', 'lst = list(range(100000))', number=100000))
print('deque.pop', timeit('my_deque.pop()',
                          'from collections import deque\nmy_deque = deque(list(range(100000)))',
                          number=100000))
print(' list.popleft', timeit('lst.pop(0)', 'lst = list(range(100000))', number=100000))
print('deque.popleft', timeit('my_deque.popleft()',
                              'from collections import deque\nmy_deque = deque(list(range(100000)))',
                              number=100000))
print(' list.reverse', timeit('lst.reverse()', 'lst = list(range(100000))', number=100000))
print('deque.reverse', timeit('my_deque.reverse()',
                              'from collections import deque\nmy_deque = deque(list(range(100000)))',
                              number=100000))
print(' list.remove', timeit('lst.remove(5)', 'lst = list(range(100))', number=1))
print('deque.remove', timeit('my_deque.remove(5)',
                             'from collections import deque\nmy_deque = deque(list(range(100)))',
                             number=1))

'''
 list 3.7409155
deque 4.7328817
 list.append 0.013731599999999997
deque.append 0.010729299999999997
 list.appendleft 12.1582645
deque.appendleft 0.010001899999998898
 list.extend 0.3070391000000008
deque.extend 0.09795860000000012
 list.pop 0.011978599999999062
deque.pop 0.013596800000000187
 list.popleft 1.2599176000000014
deque.popleft 0.00997950000000003
 list.reverse 4.967497199999999
deque.reverse 15.0634966
 list.remove 4.799999999999249e-06
deque.remove 2.799999999997249e-06

По итогам замеров list быстрее deque только при реверсе
Заполнение списка так же немного выигрывает
Примерно одинаковые результаты получены в функциях append и pop
Гораздо быстрее deque в функциях appendleft, extend, popleft
В случаях с appendleft и popleft разница понятна, список, как я понимаю,
перезаписывает все индексы, когда вставка или удаление идет вначале списка,
а вот в случае с extend не совсем поняла, ведь там тоже последовательность
вставляется в конец, однако очередь очевидно быстрее, возможно это связано с тем,
что это заложено в основном смысле работы очереди
remove отрабатывает быстрее видимо по той же причине работы с индексами
'''