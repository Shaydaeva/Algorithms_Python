"""
Задание 2.
Ваша программа должна запрашивать пароль
Для этого пароля вам нужно получить хеш, используя функцию sha256
Для генерации хеша обязательно нужно использовать криптографическую соль
Обязательно выведите созданный хеш

Далее программа должна запросить пароль повторно
Вам нужно проверить, совпадает ли пароль с исходным
Для проверки необходимо сравнить хеши паролей

ПРИМЕР:
Введите пароль: 123
В базе данных хранится строка: 555a3581d37993843efd4eba1921f1dcaeeafeb855965535d77c55782349444b
Введите пароль еще раз для проверки: 123
Вы ввели правильный пароль
"""

from uuid import uuid4
import hashlib

salt = uuid4().hex
print(f"Salt: {salt}")

user_pass = input('Enter your pass: ')

res = hashlib.sha256(salt.encode() + user_pass.encode()).hexdigest()
print(f"Password hash: {res}")

check_pass = input('Confirm your pass: ')
check_res = hashlib.sha256(salt.encode() + check_pass.encode()).hexdigest()
print(f"Password hash: {check_res}")
if res == check_res:
    print('Check passed')
else:
    print('No entry')
