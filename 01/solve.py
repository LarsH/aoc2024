# vim: et ts=4 sw=4 sts=-1
from itertools import count
from functools import lru_cache as lru, cmp_to_key

b = '''
3   4
4   3
2   5
1   3
3   9
3   3
'''

b = open('input.txt').read()
b = b.strip()


l = [e.split() for e in b.split('\n')]

l = [ (int(a), int(b)) for a,b in l]

al = [a for a, b in l]
bl = [b for a, b in l]
al.sort()
bl.sort()

o = 0
for a,b in zip(al,bl):
    c = al.count(b)
    o+= b*c

print(o)
