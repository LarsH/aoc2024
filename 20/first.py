# vim: ts=4 sw=4 et sts=-1
from itertools import count
from functools import lru_cache as lru, cmp_to_key
b = '''
###############
#...#...#.....#
#.#.#.#.#.###.#
#S#...#.#.#...#
#######.#.#.###
#######.#.#...#
#######.#.###.#
###..E#...#...#
###.#######.###
#...###...#...#
#.#####.#.###.#
#.#...#.#.#...#
#.#.#.#.#.#.###
#...#...#...###
###############
'''
b = open('input.txt').read()
b = b.strip()


l = [e for e in b.split('\n')]

l = [    e        for e in l]

for y,r in enumerate(l):
    for x,c in enumerate(r):
        if c == 'S':
            sx,sy = x,y
        elif c == 'E':
            ex,ey = x,y

def smap(x,y):
    start = (x, y)
    op = [start]
    dist = {start:0}
    while len(op) > 0:
        x,y = op.pop(0)
        td = dist[(x,y)]
        for dx,dy in [(1,0), (0,-1), (-1,0), (0,1)]:
            nt = x+dx, y+dy
            nx,ny = nt
            if l[ny][nx] == '#':
                continue
            if nt in dist:
                assert dist[nt] <= td+1
            else:
                dist[nt] = td+1
                op.append(nt)
    return dist

ds = smap(sx, sy)
de = smap(ex, ey)
assert de[sx, sy] == ds[ex, ey]
T = de[sx, sy]

o = 0
ol = []
for y in range(1,len(l)-1):
    for x in range(1,len(l[0])-1):
        c = l[y][x]
        if c != '#':
            continue
        for dx, dy in ((0,1),(1,0),(0,-1),(-1,0)):
            p1 = (x+dx,y+dy)
            p2 = (x-dx,y-dy)
            if not (p1 in ds and p2 in de):
                continue
            nt = 2 + ds[p1] + de[p2]
            save = T-nt
            if (T-nt) >= 100:
                o += 1
print(o)
# 1397
