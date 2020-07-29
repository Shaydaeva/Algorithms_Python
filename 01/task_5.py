"""
Задание 6.
Задание на закрепление навыков работы со стеком

Примечание: в этом задании вспомните ваши знания по работе с ООП
и опирайтесь на пример урока

Реализуйте структуру "стопка тарелок".

Мы можем складывать тарелки в стопку и при превышении некоторого значения
нужно начать складывать тарелки в новую стопку.

Структура должна предусматривать наличие нескольких стеков.
Создание нового стека происходит при достижении предыдущим стеком порогового значения.
Реализуйте по аналогии с примером, рассмотренным на уроке, необходимые методы,
для реализации это структуры, добавьте новые методы (не рассмотренные в примере с урока)
для реализации этой задачи.

После реализации структуры, проверьте ее работу на различных сценариях
"""


from random import randint
from math import ceil


class StackClass:
    def __init__(self):
        self.elems = []

    def is_empty(self):
        return self.elems == []

    def push_in(self, el):
        """Предполагаем, что верхний элемент стека находится в конце списка"""
        self.elems.append(el)

    def pop_out(self):
        return self.elems.pop()

    def get_val(self):
        return self.elems[len(self.elems) - 1]

    def stack_size(self):
        return len(self.elems)


# список для размещения в стек
lst = [randint(0, 100) for i in range(21)]

# максимально допустимое количество в стеке
max_value = 5

# расчет необходимого количества стеков
num_of_stack = ceil(len(lst) / max_value)

# сделала список для хранения названий стеков, так как создаю их динамически
num_var = []

# В цикле создаётся необходимое количество стеков, затем наполняется
for k in range(num_of_stack):
    num_var.append('steps_' + str(k))
    globals()['steps_' + str(k)] = StackClass()
    if len(lst) >= max_value:
        for i in range(max_value):
            globals()['steps_' + str(k)].push_in(lst[i])
        del lst[0:num_of_stack]
    elif max_value > len(lst) > 0:
        for i in range(len(lst)):
            globals()['steps_' + str(k)].push_in(lst[i])

# Выводы для наглядности
print(num_of_stack)
print(num_var)
print(steps_4.get_val())
print(steps_0.pop_out())
print(steps_0.pop_out())
print(steps_0.pop_out())
print(steps_0.pop_out())
print(steps_0.pop_out())
print(steps_3.get_val())

# и то же самое в виде функции

# список для размещения в стек
lst = [randint(0, 100) for i in range(21)]
print(lst)


def fill_stacks():
    # максимально допустимое количество в стеке
    max_value = 5

    # расчет необходимого количества стеков
    num_of_stack = ceil(len(lst) / max_value)

    # сделала список для хранения названий стеков, так как создаю их динамически
    # правда поняла, что так делать не рекомендуется
    num_var = []

    # В цикле создаётся необходимое количество стеков, затем наполняется
    for k in range(num_of_stack):
        num_var.append('steps_' + str(k))
        globals()['steps_' + str(k)] = StackClass()
        if len(lst) >= max_value:
            for i in range(max_value):
                globals()['steps_' + str(k)].push_in(lst[i])
            del lst[0:num_of_stack]
        elif max_value > len(lst) > 0:
            for i in range(len(lst)):
                globals()['steps_' + str(k)].push_in(lst[i])

# Выводы для наглядности
fill_stacks()
# print(num_of_stack)
# print(num_var)

print(steps_4.get_val())
print(steps_0.pop_out())
print(steps_0.pop_out())
print(steps_0.pop_out())
print(steps_0.pop_out())
print(steps_0.pop_out())
print(steps_3.get_val())

