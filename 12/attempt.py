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

lut = {}

def rlut(k):
    while k in lut:
        if k == lut[k]:
            break
        assert lut[k] < k
        k = lut[k]
    return k

for y in range(Y):
    for x in range(X):
        for dx,dy in ([(1,0), (0,1)]):
            nx,ny = x+dx, y+dy
            if nx >= X or ny >= Y:
                continue
            if l[y][x] != l[ny][nx]:
                continue
            p = (x,y)
            q = (nx, ny)
            u = min(rlut(p), rlut(q))
            lut[p] = u
            lut[q] = u

for y in range(Y)[::-1]:
    for x in range(X)[::-1]:
        for dx,dy in ([(-1,0), (0,-1)]):
            nx,ny = x+dx, y+dy
            if nx < 0 or ny < 0:
                continue
            if l[y][x] != l[ny][nx]:
                continue
            p = (x,y)
            q = (nx, ny)
            u = min(rlut(p), rlut(q))
            lut[p] = u
            lut[q] = u

def rek(x,y,vis,perim):
    vis.add((x,y))
    for dx,dy in ([(1,0),(0,1),(-1,0), (0,-1)]):
        nx,ny = x+dx,y+dy
        if (nx,ny) in vis:
            continue
        if rlut((nx,ny)) == rlut((x,y)):
            rek(nx, ny, vis, perim)
        else:
            p = (x,y)
            q = (nx, ny)
            perim.add((min(p,q), max(p,q)))
    return vis, perim

def meas(x,y):
    c = l[y][x]
    vis, perim = rek(x,y,set([]), set([]))
    a,b = len(vis),len(perim)
    ps = set([])
    for p,q in perim:
        ps.add(p)
        ps.add(q)
    perim = ps - vis
    mxx = max(x for x,y in vis|perim)
    myy = max(y for x,y in vis|perim)
    mnx = min(x for x,y in vis|perim)
    mny = min(y for x,y in vis|perim)
    for y in range(mny, myy+1):
        s = ''
        for x in range(mnx, mxx+1):
            if (x,y) in perim:
                s += '+'
            elif (x,y) in vis:
                s += '#'
            else:
                s += '.'
        print(s)
    print(c, a,b)
    return a*b

o = 0
for y,r in enumerate(l):
    for x,c in enumerate(r):
        p = (x,y)
        if rlut(p) == p:
            o += meas(x,y)
print(o)
# 1087308
# 1435856
