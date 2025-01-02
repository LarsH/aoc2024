# vim: ts=4 sw=4 et sts=-1
from itertools import count
from functools import lru_cache as lru, cmp_to_key
b = '''
RRRRIICCFF
RRRRIICCCF
VVRRRCCFFF
VVRCCCJFFF
VVVVCJJCFE
VVIVCCJJEE
VVIIICJJEE
MIIIIIJJEE
MIIISIJEEE
MMMISSJEEE
'''
b = open('input.txt').read()
b = b.strip()

l = [e for e in b.split('\n')]
l = [    list(e)        for e in l]

X = len(l[0])
Y = len(l)

def rek(x,y,c,vis):
    vis.add((x,y))
    perim = 0
    for dx,dy in ([(1,0),(0,1),(-1,0), (0,-1)]):
        nx,ny = x+dx,y+dy

        if (nx,ny) in vis:
            continue

        isInside = True
        if nx < 0 or ny < 0 or nx >= X or ny >= Y:
            isInside = False

        if isInside and l[ny][nx] == c:
            perim += rek(nx, ny, c, vis)
        else:
            perim += 1

    return perim

o = 0

visited = set([])
for y,r in enumerate(l):
    for x,c in enumerate(r):
        if not (x,y) in visited:
            vis = set([])
            b = rek(x,y,c,vis)
            visited |= vis
            a = len(vis)
            print(c, a,b)
            o += a*b

print(o)
# 1087308
# 1435856
