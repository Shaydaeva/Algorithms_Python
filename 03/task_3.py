"""
Задание 3.
Определить количество различных подстрок с использованием хеш-функции.
Дана строка S длиной N, состоящая только из строчных латинских букв.

Подсказка: примените хеши и множества

рара:

рар
ра
ар
ара
р
а
"""

import hashlib

s = 'papa'
s_set = set()

for i in range(len(s)):
    for j in range(len(s)+1):
        if j > i and not(i == 0 and j == (len(s))):
            s_set.add(s[i:j])

print(len(s_set))


def substrings(s, h_set=set()):
    for i in range(len(s)):
        for j in range(len(s) + 1):
            if j > i and not (i == 0 and j == (len(s))):
                h_set.add(hashlib.sha256(s[i:j].encode()).hexdigest())
    return len(h_set)


print(substrings(s))
