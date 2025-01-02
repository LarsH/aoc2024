# vim: ts=4 sw=4 et sts=-1
from itertools import count
from functools import lru_cache as lru, cmp_to_key
b = '''
....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...
'''
b = open('input.txt').read()
b = b.strip()


l = [e for e in b.split('\n')]
l = [    e        for e in l]
Y = len(l)
X = len(l[0])


for ty,t in enumerate(l):
    if not '^' in t:
        continue
    for tx,c in enumerate(t):
        if c == '^':
            x,y = tx,ty
            gd = 0
            break
    else:
        assert False
    break
else:
    assert False

o = 0
dl = [(0,-1), (1,0), (0,1),(-1,0)]
vis = set([(x,y)])
while True:
    dx,dy = dl[gd]
    nx,ny = x+dx,y+dy
    if not(0<=nx<X and 0<=ny<Y):
        break
    if l[ny][nx] == '#':
        gd = (gd+1)%4
    else:
        x,y = nx,ny
        vis.add((x,y))

print(len(vis))

