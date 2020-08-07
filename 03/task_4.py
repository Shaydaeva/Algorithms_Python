"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если нет, то вносит ее в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования
Можете условжнить задачу, реализовав ее через ООП
"""
from uuid import uuid4
import hashlib


salt_url_cash = uuid4().hex


def check_url(url, memory_url={}):
    if url not in memory_url.keys():
        memory_url[url] = hashlib.sha256(salt_url_cash.encode() + url.encode()).hexdigest()
    return memory_url


a = 'https://ru.wikipedia.org/wiki/Mitchell_Camera'
print(check_url(a))

# для прохождения в цикле с вводом
# a = ''
# while a!='0':
#     a = input('Enter url: ')
#     print(check_url(a))
