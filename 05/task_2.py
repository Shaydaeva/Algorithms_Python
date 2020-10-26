"""
2.	Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как массив, элементы которого это цифры числа.
Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’]
соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

Подсказка:
Для решения задачи обязательно примените какую-нибудь коллекцию из модуля collections
Для лучшее освоения материала можете даже сделать несколько решений этого задания,
применив несколько коллекций из модуля collections
Также попробуйте решить задачу вообще без collections и применить только ваши знания по ООП
(в частности по перегрузке методов)
"""
from collections import defaultdict

first_num = input('Введите первое число: ')
second_num = input('Введите второе число: ')
num_list = [first_num, second_num]
hex_dict = defaultdict(list)

for i in range(2):
    hex_dict[num_list[i]].extend(list(num_list[i]))

print(hex_dict)
print(hex_dict[first_num])

summ = hex(int(first_num, 16) + int(second_num, 16))
hex_dict[summ[2:].upper()].append(list(summ[2:].upper()))
print(f'Cумма: {summ[2:].upper()}')

mult = hex(int(first_num, 16) * int(second_num, 16))
hex_dict[mult[2:].upper()].append(list(mult[2:].upper()))
print(f'Произведение: {mult[2:].upper()}')

print(hex_dict)
