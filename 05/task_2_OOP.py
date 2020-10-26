"""
Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’]
соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
"""


class HexNumber:
    def __init__(self, num):
        self.num = num

    def __add__(self, other):
        res = hex(int(self.num, 16) + int(other.num, 16))
        return f'Сумма: {list(res[2:].upper())}'

    def __mul__(self, other):
        res = hex(int(self.num, 16) * int(other.num, 16))
        return f'Произведение: {list(res[2:].upper())}'


x = HexNumber('A2')
y = HexNumber('C4F')
print(x + y)
print(x * y)
