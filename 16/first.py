# vim: ts=4 sw=4 et sts=-1
from itertools import count
from functools import lru_cache as lru, cmp_to_key
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
while len(op):
    (cost, x, y, d) = heapq.heappop(op)
    t = (x,y,d)
    if t in visited:
        continue
    visited.add(t)

    dx, dy = dl[d]
    nx, ny = x+dx, y+dy
    if nx == ex and ny == ey:
        print(cost + 1)
        break
    elif l[ny][nx] != '#':
        heapq.heappush(op, (cost+1, nx, ny, d))
    heapq.heappush(op, (cost+1000, x, y, (d+1)%4))
    heapq.heappush(op, (cost+1000, x, y, (d+3)%4))
