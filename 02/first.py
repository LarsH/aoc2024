# vim: ts=4 sw=4 et sts=-1
from itertools import count
from functools import lru_cache as lru, cmp_to_key
b = '''
7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
'''
b = open('input.txt').read()
b = b.strip()


l = [e for e in b.split('\n')]

l = [[int(x) for x in    e.split()]       for e in l]

o = 0
for x in l:
    safe = True
    for a,b in zip(x,x[1:]):
        if abs(a-b) > 3 or abs(a-b) < 1:
            safe = False
        if not((a<b) == (x[0]<x[1])):
            safe = False
    if safe:
        o += 1
print(o)
