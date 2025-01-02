# vim: ts=4 sw=4 et sts=-1
from itertools import count
from functools import lru_cache as lru, cmp_to_key
b = '''
125 17
'''
b = open('input.txt').read()
b = b.strip()

l = [int(e) for e in b.split()]

def f(x):
    if x == 0:
        return [1]
    t = str(x)
    q = len(t)
    if q%2 == 0:
        return [int(t[:q//2]), int(t[q//2:])]
    else:
        return [x*2024]
@lru(maxsize=None)
def rek(x,n):
    if n == 0:
        return 1
    if x == 0:
        return rek(1, n-1)
    t = str(x)
    q = len(t)
    if q%2 == 0:
        return rek(int(t[:q//2]), n-1) + rek( int(t[q//2:]), n-1)
    else:
        return rek(x*2024, n-1)

print(sum([rek(x, 75) for x in l]))
