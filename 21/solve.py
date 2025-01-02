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

seen = set([])
o = 0
# gather pieces
for c in l:
    c = seq(c, NUM)
    for x in c:
        seen |= set(x.split('A'))
    pseen = None
    for _ in range(20):
        pseen = seen
        c = (sum((seq(e+'A', DIR) for e in ''.join(e+'A' for e in sorted(seen))), []))
        for x in c:
            seen |= set(x.split('A'))

# find minimal replacements
LUT = {}
for x in seen:
    ll = seq(x+'A', DIR)
    m = (float('inf'), 'X')
    if len(ll) == 1:
        t = ll[0][:-1].split('A')
    else:
        for e in ll:
            print(e)
            y = minl(seq(e, DIR))
            #y = minl(sum((seq(ee, DIR) for ee in y), []))
            m = min(m, min((len(z),e) for z in y))
        #print(m[1])
        t = m[1][:-1].split('A')
    d = {k:t.count(k) for k in set(t)}
    print(x, d)
    LUT[x] = d

def qml(s, n):
    global LUT
    assert s[-1] == 'A'
    t = s[:-1].split('A')
    d = {k:t.count(k) for k in set(t)}
    for _ in range(n):
        nd = {}
        for k,v in d.items():
            assert k in LUT, (k, LUT)
            for rk, vk in LUT[k].items():
                nd[rk] = nd.get(rk,0) + v*vk
        d = nd
    return sum((1+len(k))*v for k,v in d.items())

@lru(None)
def rek(s, n):
    assert s[-1] == 'A'
    if n == 0:
        return len(s)

    retval = 0
    for p in s[:-1].split('A'):
        tries = seq(p+'A', DIR)
        retval += min(rek(t, n-1) for t in tries)
    return retval

# do quick compute
o = 0
for c in l:
    print(c)
    cl = seq(c, NUM)
    m = min(rek(x, 25) for x in cl)
    o += int(c.replace('A','')) * m
print(o)

# 98585568833228 24 too low
# 246778413153978 25
# 617733235787280 26 too high
# 216668579770346

