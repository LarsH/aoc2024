# vim: ts=4 sw=4 et sts=-1
from itertools import count
from functools import lru_cache as lru, cmp_to_key
b = '''
1
10
100
2024
'''
b = open('input.txt').read()
b = b.strip()


l = [e for e in b.split('\n')]

l = [  int(  e )       for e in l]


def round(x):
    x = x ^ (x*64)
    x %= 16777216
    x = x ^ (x//32)
    x %= 16777216
    x = x ^ (x*2048)
    x %= 16777216
    return x

o = 0
for x in l:
    for _ in range(2000):
        x = round(x)
    o += x

print(o)
