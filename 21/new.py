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
b = open('input.txt').read()
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
    return tuple('AND', *ol)

def rseq(x, keyb):
    if isinstance(x, str):
        return seq(x, keyb)
    elif x[0]== 'AND':
        return tuple('AND', rseq(y, keyb) for y in x[1:])
    else:
        assert isinstance(x, str)

def _norm(x):
    if isinstance(x, str):
        return x
    elif len(x) == 2:
        return x[1]
    elif isinstance(XXXXXXXX, tuple):
        if all(isinstance(e, str) for e in x):
            return ''.join(x)
        else:
            return tuple(_norm(e) for e in x)
    elif isinstance(x, list):
        return [_norm(e) for e in x]
    else:
        assert isinstance(x, str)
        return x

def norm(x):
    px = None
    while px != x:
        px = x
        x = _norm(x)
    return x

def minify(x):
    # returns len, data
    if isinstance(x, str):
        return len(x), x
    elif x[0] == 'AND':
        rl = [minify(y) for y in x[1:]]
        return sum(a for a,b in rl), tuple('AND', *(b for a,b in rl))
    elif x[0] == 'OR':
        rl = [minify(y) for y in x[1:]]
        ml = min(a for a,b in rl)
        return ml, tuple('OR', *(b for a,b in rl if a == ml))
    else:
        assert False, x

o = 0
for c in l:
    print('=====')
    print(c)
    # c : str
    c = norm(minify(rseq(c, NUM))[1])
    # c1 : tuple of list  of strings
    for i in range(25):
        c = norm(c)
        print('x')
        ll, c = minify(rseq(c, DIR))
        print(i, ll)
        print(c)
    o += int(c.replace('A','')) * ll

print(o)
