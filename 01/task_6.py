"""
Задание 7.
Задание на закрепление навыков работы с очередью

Примечание: в этом задании вспомните ваши знания по работе с ООП
и опирайтесь на пример урока

Реализуйте структуру "доска задач".


Структура должна предусматривать наличие несольких очередей задач, например
1) базовой, откуда задачи берутся, решаются и отправляются в список решенных
2) очередь на доработку, когда нерешенные задачи из первой очереди отправляются
на корректировку решения

После реализации структуры, проверьте ее работу на различных сценариях
"""

from random import randint


class QueueClass:
    def __init__(self):
        self.elems = []

    def is_empty(self):
        return self.elems == []

    def to_queue(self, item):
        self.elems.insert(0, item)

    def from_queue(self):
        return self.elems.pop()

    def size(self):
        return len(self.elems)

"""
Проверка значения, после совершенного с ним действия
"""

lst = [randint(0, 9) for i in range(21)]    # список дел
print(lst)
process = 3     # действие
total = 10      # что нужно было получить

queue_base = QueueClass()
queue_turn = QueueClass()

for i in lst:
    queue_base.to_queue(i)

while not queue_base.is_empty():
    task = queue_base.from_queue()
    if task + process < total:
        queue_turn.to_queue(task)
    print(queue_base.size(), queue_turn.size())

