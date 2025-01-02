# vim: ts=4 sw=4 et sts=-1
from itertools import count
from functools import lru_cache as lru, cmp_to_key
b = '''
190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20
'''
b = open('input.txt').read()
b = b.strip()


l = [e for e in b.split('\n')]

l = [e.split(':')        for e in l]
print(l)
l = [(int(a), [int(x) for x in b.strip().split(' ')]) for a,b in l]

import math
def check(l, target, acc):
    if acc > target:
        return False
    if len(l) == 0:
        return acc == target
    a,*b = l
    if check(b, target, acc*a) or check(b, target, acc+a):
        return True
    t = int(math.log(99) / math.log(10))
    q = (t*(10**t)) + a
    return check(b, target, q)

o = 0
for a,b in l:
    if check(b[1:], a, b[0]):
        print(o)
        o += a
print(o)
