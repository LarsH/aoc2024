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
            sx,sy = tx,ty
            gd = 0
            break
    else:
        assert False
    break
else:
    assert False

dl = [(0,-1), (1,0), (0,1),(-1,0)]

def first(x,y):
    gd = 0
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
    return vis

def check(x,y,ax,ay):
    gd = 0
    vis = set([(x,y,gd)])
    while True:
        dx,dy = dl[gd]
        nx,ny = x+dx,y+dy
        if not(0<=nx<X and 0<=ny<Y):
            return False
        if l[ny][nx] == '#' or ((nx,ny) == (ax,ay)):
            gd = (gd+1)%4
        else:
            x,y = nx,ny
            if (x,y,gd) in vis:
                return True
            vis.add((x,y,gd))

o = 0
pp = first(sx, sy)
for ax,ay in pp:
    if check(sx,sy, ax,ay):
        o += 1
print(o)
