from collections import OrderedDict
from timeit import timeit

print('dict', timeit('{str(i):i for i in range(1000)}', number=1000))
print('OrdD', timeit('OrderedDict((str(i), i) for i in range(1000))',
                     'from collections import OrderedDict',
                     number=1000))
print('dict.popitem', timeit('d.popitem()', 'd={str(i):i for i in range(1000)}', number=1000))
print('OrdD.popitem', timeit('ord_d.popitem()',
                             'from collections import OrderedDict\n'
                             'ord_d=OrderedDict((str(i), i) for i in range(1000))',
                             number=1000))
print('dict +', timeit("""for i in range(1001, 2000):
                          d[i]=i""",
                       'd={str(i):i for i in range(1000)}',
                       number=1000))
print('OrdD +', timeit("""for i in range(1001, 2000):
                          ord_d[i]=i""",
                       'from collections import OrderedDict\n'
                       'ord_d=OrderedDict((str(i), i) for i in range(1000))',
                       number=1000))

"""
По результатам замеров на Python 3.8 обычный словарь работает быстрее

dict 0.565913
OrdD 0.8472308000000001
dict.popitem 0.00015279999999995297
OrdD.popitem 0.00026100000000006673
dict + 0.15590740000000003
OrdD + 0.20034940000000012
"""
