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

for x in range(25):
    print(x)
    l = sum([f(x) for x in l], [])
print(len(l))
