"""
1.	Пользователь вводит данные о количестве предприятий, их наименования и прибыль
за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия.
Программа должна определить среднюю прибыль (за год для всех предприятий)
и вывести наименования предприятий, чья прибыль выше среднего и отдельно
вывести наименования предприятий, чья прибыль ниже среднего.

Подсказка:
Для решения задачи обязательно примените какую-нибудь коллекцию из модуля collections
Для лучшее освоения материала можете даже сделать несколько решений этого задания,
применив несколько коллекций из модуля collections

Пример:
Введите количество предприятий для расчета прибыли: 2
Введите название предприятия: Рога
через пробел введите прибыль данного предприятия
за каждый квартал(Всего 4 квартала): 235 345634 55 235

Введите название предприятия: Копыта
через пробел введите прибыль данного предприятия
за каждый квартал(Всего 4 квартала): 345 34 543 34

Средняя годовая прибыль всех предприятий: 173557.5
Предприятия, с прибылью выше среднего значения: Рога

Предприятия, с прибылью ниже среднего значения: Копыта
"""
from collections import Counter
from collections import defaultdict

number_of_enterprises = int(input('Введите количество предприятий для расчета прибыли: '))
enterprise_profit = defaultdict(list)
for i in range(number_of_enterprises):
    company_name = input('Введите название предприятия: ')
    profit = input('через пробел введите прибыль данного предприятия '
                   'за каждый квартал(Всего 4 квартала): ').split()
    if len(profit) == 4:
        for j in range(4):
            profit[j] = int(profit[j])
    enterprise_profit[company_name] = profit

# Для проверки
# enterprise_profit = defaultdict(list, {'wewe': [1, 2, 3, 4], 'qq': [2, 3, 4, 5], 'aa': [3, 4, 5, 6]})
c = Counter()
for i in enterprise_profit:
    c[i] = sum(enterprise_profit[i])
print(c)
av_pr = 0

for i in c:
    av_pr += (c[i])

av_pr = av_pr/len(c)
print(av_pr)

# Добавила сразу в print, хотя наверно так было нагляднее
# above = list(i for i in c if c[i] >= av_pr)
# below = list(i for i in c if c[i] < av_pr)

print(f'Средняя годовая прибыль всех предприятий: {av_pr}\n\n'
      f'Предприятия, с прибылью выше среднего значения: {", ".join(list(i for i in c if c[i] >= av_pr))}\n\n'
      f'Предприятия, с прибылью ниже среднего значения: {", ".join(list(i for i in c if c[i] < av_pr))}')

# Обычное решение
# number_of_enterprises = int(input('Введите количество предприятий для расчета прибыли: '))
# enterprise_profit = {}
# for i in range(number_of_enterprises):
#     company_name = input('Введите название предприятия: ')
#     profit = input('через пробел введите прибыль данного предприятия '
#                    'за каждый квартал(Всего 4 квартала): ').split()
#     if len(profit) == 4:
#         for j in range(4):
#             profit[j] = int(profit[j])
#     average_profit = sum(profit)
#     enterprise_profit[company_name] = average_profit
#     print(enterprise_profit)

# enterprise_profit = {'wewe': 2.5, 'qq': 4.5, 'qwe': 3}
# av_pr = 0
# for i in enterprise_profit:
#     av_pr += enterprise_profit.get(i)
# av_pr = av_pr/len(enterprise_profit)
# above = []
# below = []
# for k, v in enterprise_profit.items():
#     if v > av_pr:
#         above.append(k)
#     else:
#         below.append(k)
#
# print(f'Средняя годовая прибыль всех предприятий: {av_pr}\n\n'
#       f'Предприятия, с прибылью выше среднего значения: {", ".join(above)}\n\n'
#       f'Предприятия, с прибылью ниже среднего значения: {", ".join(below)} \n\n')
