# vim: ts=4 sw=4 et sts=-1
from itertools import count
from functools import lru_cache as lru, cmp_to_key
b = '''
............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............

'''
b = open('input.txt').read()
b = b.strip()

import itertools

l = [e for e in b.split('\n')]
l = [    e        for e in l]
ant = set(b.replace('\n','').replace('.',''))
print(ant)

X = len(l[0])
Y = len(l)

antp = set([])
ants= {a:[] for a in ant}
for y,rw in enumerate(l):
    for x, c in enumerate(rw):
        if c == '.':
            continue
        ants[c].append((x,y))

seen = set([])
for a,pl in ants.items():
    print(a, pl)
    for (x1,y1), (x2,y2) in itertools.combinations(pl, 2):
        dx = x2-x1
        dy = y2-y1
        seen.add((x2+dx, y2+dy))
        seen.add((x1-dx, y1-dy))
fs = set((x,y) for x,y in seen if (0<=x<X and 0<=y<Y))
'''
for y,rw in enumerate(l):
    s = ''
    for x, c in enumerate(rw):
        if c != '.':
            s += (c)
        else:
            if (x,y) in seen:
                s += ('#')
            else:
                s += ('.')
    print(s)
'''

print(len(fs))
