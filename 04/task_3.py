"""
Задание 3.

Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.

Сделайте профилировку каждого алгоритма через cProfile и через timeit

Сделайте вывод, какая из трех реализаций эффективнее и почему
-------------------------------------------------------------

Наиболее эффекивная 3-яя реализация, что вполне ожидаемо, т.к.
там используется встроенная функция и срез, без рекурсивных вызовов.
И это единсвенная функция, которая возвращает верный ответ.

Первые две изменила, чтобы они так же возвращали верный ответ.
Полагаю, что вторая функция чуть быстрее первой из-за наличия рекурсии в первой,
а во второй аналогичный функционал прорабаатывает цикл while
"""
import cProfile
from timeit import timeit


def revers(enter_num, revers_num=0):
    if enter_num == 0:
        return int(revers_num)
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        return revers(enter_num, revers_num)


def revers_2(enter_num, revers_num=0):
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return int(revers_num)


def revers_3(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num


def main():
    revers(12345678901234567890)
    revers_2(12345678901234567890)
    revers_3(12345678901234567890)


print(revers(12345))
print(revers_2(12345))
print(revers_3(12345))

print(timeit("revers(12345)", "from __main__ import revers"))
print(timeit("revers_2(12345)", "from __main__ import revers_2"))
print(timeit("revers_3(12345)", "from __main__ import revers_3"))
cProfile.run('revers(12345678901234567890)')
cProfile.run('revers_2(12345678901234567890)')
cProfile.run('revers_3(12345678901234567890)')

cProfile.run('main()')
