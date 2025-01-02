# vim: ts=4 sw=4 et sts=-1
from itertools import count
from functools import lru_cache as lru, cmp_to_key
b = '''
#####
.####
.####
.####
.#.#.
.#...
.....

#####
##.##
.#.##
...##
...#.
...#.
.....

.....
#....
#....
#...#
#.#.#
#.###
#####

.....
.....
#.#..
###..
###.#
###.#
#####

.....
.....
.....
#....
#.#..
#.#.#
#####
'''
b = open('input.txt').read()
b = b.strip()


l = [e for e in b.split('\n\n')]

l = [    e.split('\n') for e in l]

locks = []
keys= []
for e in l:
    if e[0][0] == '.':
        locks.append(e)
    else:
        keys.append(e)

o = 0
for l in locks:
    for k in keys:
        overlap = False
        for a,b in zip(l,k):
            for i,j in zip(a,b):
                if i == '#' and j == '#':
                    overlap = True
        if not overlap:
            o += 1
print(o)
