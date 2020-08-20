"""
Задание 5.*

Приведен наивный алгоритм нахождения i-го по счёту
простого числа (через перебор делителей).

Попробуйте решить эту же задачу,
применив алгоритм "Решето эратосфена" (https://younglinux.info/algorithm/sieve)

Подсказка:
Сравните алгоритмы по времени на разных порядковых номерах чисел:
10, 100, 1000
Опишите результаты, сделайте выводы, где и какой алгоритм эффективнее
Подумайте и по возможности определите сложность каждого алгоритма
"""
from timeit import timeit


def simple(i):
    """Без использования «Решета Эратосфена»"""
    count = 1
    n = 2
    while count <= i:
        t = 1
        is_simple = True
        while t <= n:
            if n % t == 0 and t != 1 and t != n:
                is_simple = False
                break
            t += 1
        if is_simple:
            if count == i:
                break
            count += 1
        n += 1
    return n


def simple_func(n):
    a = []
    for i in range(n+1):
        a.append(i)
    a[1] = 0
    i = 2
    while i <= n:
        if a[i] != 0:
            j = i + i
            while j <= n:
                a[j] = 0
                j = j + i
        i += 1
    simple_nums = [i for i in a if i != 0]
    return simple_nums


def eratosthenes(n):     # n - число, до которого хотим найти простые числа
    sieve = list(range(n + 1))
    sieve[1] = 0
    for i in sieve:
        if i > 1:
            for j in range(i + i, len(sieve), i):
                sieve[j] = 0
    sieve1 = [x for x in sieve if sieve[x] != 0]
    return sieve1


def num_simple_eratosthenes(n):  # n-ое по счету простое число
    i = 2
    l = 10000
    sieve = list(range(l))
    sieve[1] = 0
    while i < l:
        if sieve[i] != 0:
            m = i * 2
            while m < l:
                sieve[m] = 0
                m += i
        i += 1
    return [x for x in sieve if x != 0][n-1]


print('Обычный   ', timeit('simple_func(100)', 'from __main__ import simple_func', number=100))
print('С решетом ', timeit('eratosthenes(100)', 'from __main__ import eratosthenes', number=100))
print('Обычный   ', timeit('simple_func(1000)', 'from __main__ import simple_func', number=100))
print('С решетом ', timeit('eratosthenes(1000)', 'from __main__ import eratosthenes', number=100))
print('Обычный   ', timeit('simple_func(10000)', 'from __main__ import simple_func', number=100))
print('С решетом ', timeit('eratosthenes(10000)', 'from __main__ import eratosthenes', number=100))
print()
print('Обычный   ', timeit('simple(10)', 'from __main__ import simple', number=10))
print('С решетом ', timeit('num_simple_eratosthenes(10)', 'from __main__ import num_simple_eratosthenes', number=10))
print('Обычный   ', timeit('simple(100)', 'from __main__ import simple', number=10))
print('С решетом ', timeit('num_simple_eratosthenes(100)', 'from __main__ import num_simple_eratosthenes', number=10))
print('Обычный   ', timeit('simple(1000)', 'from __main__ import simple', number=10))
print('С решетом ', timeit('num_simple_eratosthenes(1000)', 'from __main__ import num_simple_eratosthenes', number=10))

'''
Для выявления списка простых чисел функция с применением решета при 
обработке больших чисел работает немного быстрее, однако алгоритм
нахождения i-го по счёту простого числа с применением решета показывает 
стабильные значения вне зависимости от количества обрабатываемых данных,
что при увеличении обрабатываемых данных дает внушительную разницу

Обычный    0.0097077
С решетом  0.004906700000000007
Обычный    0.09761560000000001
С решетом  0.0529915
Обычный    0.9985671999999999
С решетом  0.6146161000000001

Обычный    0.0004205999999999932
С решетом  0.0855075999999999
Обычный    0.05330159999999995
С решетом  0.09929480000000002
Обычный    9.6835089
С решетом  0.08320860000000074'''
