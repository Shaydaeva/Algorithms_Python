from collections import Counter, deque


def haffman_code(s):
    count = Counter(s)
    coded = deque(sorted(count.items(), key=lambda item: item[1]))
    # как вариант сортровки
    # coded = deque(count.most_common()[::-1])
    if len(coded) != 1:
        # Цикл для построения дерева
        while len(coded) > 1:
            k_1, v_1 = coded.popleft()
            k_2, v_2 = coded.popleft()
            summ = v_1 + v_2
            # Переписала заполнение дерева
            if type(k_1) == dict or type(k_2) == dict:
                if isinstance(k_1, dict):
                    comb = dict()
                    for k, v in k_1.items():
                        comb[k] = '0' + v
                else:
                    comb = {k_1: '0'}
                if isinstance(k_2, dict):
                    for k, v in k_2.items():
                        comb[k] = '1' + v
                else:
                    comb[k_2] = '1'
            else:
                comb = {k_1: '0', k_2: '1'}

            # Ищем место для ставки объединенного элемента
            for i, el in enumerate(coded):
                if summ >= el[1]:
                    continue
                else:
                    coded.insert(i, (comb, summ))
                    break
            else:
                coded.append((comb, summ))
    else:
        # приравниваемыем значение 0 к одному повторяющемуся символу
        k_1, v_1 = coded.popleft()
        comb = {k_1: '0'}
        coded.append((comb, v_1))
    return coded[0][0]


s = "beep boop beer!"
code_table = haffman_code(s)
for i in s:
    print(code_table[i], end=' ')
print()
