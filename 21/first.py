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
    ol = ['']
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
        x,y = nx,ny

        tmp = []
        for a in ol:
            for b in pts:
                tmp.append(a+b)
        ol = tmp
    return (ol)

def minl(ol):
    ml = min(len(e) for e in ol)
    k = [e for e in ol if len(e) == ml]
    return k

o = 0
for c in l:
    print('=====')
    print(c)
    c1 = seq(c, NUM)
    c2 = minl(sum((seq(e, DIR) for e in c1), []))
    c3 = minl(sum((seq(e, DIR) for e in c2), []))
    o += int(c.replace('A','')) * len(c3[0])

print(o)
