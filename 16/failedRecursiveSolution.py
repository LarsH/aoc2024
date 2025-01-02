# vim: ts=4 sw=4 et sts=-1
from itertools import count
from functools import lru_cache as lru, cmp_to_key
import sys
sys.setrecursionlimit(3000)

b = '''
###############
#.......#....E#
#.#.###.#.###.#
#.....#.#...#.#
#.###.#####.#.#
#.#.#.......#.#
#.#.#####.###.#
#...........#.#
###.#.#####.#.#
#...#.....#.#.#
#.#.#.###.#.#.#
#.....#...#.#.#
#.###.#.#.#.#.#
#S..#.....#...#
###############
'''
b = open('input.txt').read()
b = b.strip()

l = [e for e in b.split('\n')]
l = [    list(e)        for e in l]

for y,r in enumerate(l):
    for x,c in enumerate(r):
        if c == 'S':
            sx,sy = x,y
        if c == 'E':
            ex,ey = x,y

dl = [(1,0), (0,-1), (-1,0), (0,1)]
visited = set([])

op = [(0, sx, sy, 0)]
import heapq
mc = None

while len(op):
    (cost, x, y, d) = heapq.heappop(op)

    if mc is not None:
        if cost > mc:
            break

    t = (x,y,d)
    if t in visited:
        continue
    visited.add(t)

    if x == ex and y == ey:
        mc = cost
        continue

    dx, dy = dl[d]
    nx, ny = x+dx, y+dy
    if l[ny][nx] != '#':
        heapq.heappush(op, (cost+1, nx, ny, d))
    heapq.heappush(op, (cost+1000, x, y, (d+1)%4))
    heapq.heappush(op, (cost+1000, x, y, (d+3)%4))
print(mc)

bestpath = set() # (x, y, d)
rcost = {}
def rek(cost, x, y, d):
    if cost > mc:
        return False
    t = (x,y,d)
    if not t in visited:
        return False
    if not t in rcost:
        rcost[t] = cost
    else:
        if rcost[t] < cost:
            return False

    if x == ex and y == ey:
        bestpath.add((x,y))
        return True

    dx, dy = dl[d]
    nx, ny = x+dx, y+dy

    a = rek(cost+1, nx, ny, d)
    b = rek(cost+1000, x, y, (d+1)%4)
    c = rek(cost+1000, x, y, (d+3)%4)

    if a or b or c:
        bestpath.add((x,y))
        return True
    else:
        return False


rek(0, sx, sy, 0)
print(len(bestpath))
