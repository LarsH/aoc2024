# vim: ts=4 sw=4 et sts=-1
from itertools import count, permutations
from functools import lru_cache as lru, cmp_to_key
b = '''
029A
980A
179A
456A
379A
'''
#b = open('input.txt').read()
b = b.strip()

l = [e for e in b.split('\n')]
l = [    e        for e in l]

NUM = '789\n456\n123\n.0A'.split('\n')
DIR = '.^A\n<v>'.split('\n')

def getpos(target, keyb):
    for y,r in enumerate(keyb):
        for x,c in enumerate(r):
            if c == target:
                return x,y
    assert False

def seq(target:str, keyb, start='A'):
    x,y = getpos(start, keyb)
    ol = []
    for c in target:
        nx,ny = getpos(c, keyb)
        dx,dy = nx-x, ny-y
        if dx > 0:
            xc = '>'
        else:
            xc = '<'
        if dy > 0:
            yc = 'v'
        else:
            yc = '^'

        pts = []
        for e in set(permutations(xc*abs(dx)+yc*abs(dy))):
            tx, ty = x,y
            for c in e:
                dx,dy = {'>':(1,0),'<':(-1,0),'^':(0,-1),'v':(0,1)}[c]
                tx,ty = tx+dx,ty+dy
                if keyb[ty][tx] == '.':
                    break
            else:
                # valid path
                pts.append(''.join(e)+'A')
        ol.append(pts)
        x,y = nx,ny
    return tuple(ol)

def normalize(x):
    if len(x) == 1:
        return x[0]

    elif isinstance(x, tuple):
        if all(isinstance(e, str) for e in x):
            return ''.join(x)
        else:
            return tuple(normalize(e) for e in x)
    elif isinstance(x, list):
        return [normalize(e) for e in x]
    else:
        assert isinstance(x, str)
        return x

def rnorm(x):
    px = None
    while px != x:
        px = x
        x = normalize(x)
    return x

for c in l:
    print('=====')
    print(c)
    c1 = rnorm(seq(c, NUM))
    print(c1)
    c2 = rnorm(tuple([seq(e, DIR) for e in a] for a in c1))
    for c in c2:
        print('... ', rnorm(c2))
    break
