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

b2 = '''
AAAAAA
AAABBA
AAABBA
ABBAAA
ABBAAA
AAAAAA
'''

b4 = '''
EEEEE
EXXXX
EEEEE
EXXXX
EEEEE
'''

b = open('input.txt').read()
b = b.strip()

l = [e for e in b.split('\n')]
l = [    list(e)        for e in l]

X = len(l[0])
Y = len(l)


'''
pole is upper left corner
'''

def rek(x,y,c,vis):
    vis.add((x,y))
    perim = set([])
    for dx,dy,p1,p2 in ([(1,0,(1,0),(1,1)),
                            (0,1,(1,1),(0,1)),
                            (-1,0,(0,1),(0,0)),
                            (0,-1,(0,0),(1,0))
                            ]):
        nx,ny = x+dx,y+dy

        if (nx,ny) in vis:
            continue

        isInside = True
        if nx < 0 or ny < 0 or nx >= X or ny >= Y:
            isInside = False

        if isInside and l[ny][nx] == c:
            perim |= rek(nx, ny, c, vis)
        else:
            perim.add(tuple((x+dx, y+dy) for dx,dy in [p1,p2]))
    return perim

o = 0


import matplotlib


def getFenceLayer(perim):
    visited = set([])
    dl = [(1,0), (0,1), (-1,0), (0,-1)]

    turns = 0
    start = min(perim)
    this = start
    nxt = None
    pl = [this[0]]

    while nxt != start:
        visited.add(this)
        pl.append(this[1])
        d  = (this[1][0] - this[0][0], this[1][1] - this[0][1])
        assert d in dl
        i = dl.index(d)
        for q in [3,0,1]:
            dx,dy = dl[(i+q)%4]
            nxt = (this[1], (this[1][0] + dx, this[1][1] + dy))
            #print(d,(dx,dy), this, nxt)
            if nxt in perim:
                if q != 0:
                    turns += 1
                break
        else:
            assert False, this

        this = nxt

    left = perim - visited
    if len(left):
        print('getting moar')
        turns += getFenceLayer(left)
    return turns

visited = set([])
for y,r in enumerate(l):
    for x,c in enumerate(r):
        if not (x,y) in visited:
            vis = set([])
            perim = rek(x,y,c,vis)
            visited |= vis
            a = len(vis)
            b = getFenceLayer(perim)
            #print(c, a, b)
            o += a*b
print(o)
