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


def rek(x,y):
    start = (x, y)
    op = [start]
    dist = {start:0}
    rval = {}
    while len(op) > 0:
        x,y = op.pop(0)
        td = dist[(x,y)]
        if td > 19:
            continue
        for dx,dy in [(1,0), (0,-1), (-1,0), (0,1)]:
            nt = x+dx, y+dy
            nx,ny = nt
            if not((0<=nx<len(l[0])) and (0<=ny<len(l))):
                continue

            if nt in dist:
                assert dist[nt] <= td+1
                continue
            dist[nt] = td+1
            op.append(nt)
            if l[ny][nx] != '#':
                rval[nt] = min(rval.get(nt, 99), td+1)
    return rval


ds = smap(sx, sy)
de = smap(ex, ey)
assert de[sx, sy] == ds[ex, ey]
T = de[sx, sy]

o = 0
ol = []
for y in range(len(l)):
    for x in range(len(l[0])):
        c = l[y][x]
        if c == '#':
            continue
        sk = rek(x, y)
        #print(sk)

        for (ox, oy),ex in sk.items():
            p1 = (x, y)
            p2 = (ox, oy)
            assert (p1 in ds and p2 in de)
            nt = ex + ds[p1] + de[p2]
            save = T-nt
            if save >= 50:
                ol.append(save)
            if save >= 100:
                o += 1

#for t in sorted(set(ol)):
#    print(ol.count(t), t)

print('----\n', o)

