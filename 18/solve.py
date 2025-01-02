# vim: ts=4 sw=4 et sts=-1
from itertools import count
from functools import lru_cache as lru, cmp_to_key
b = '''
'''
b = open('input.txt').read()
b = b.strip()


l = [e for e in b.split('\n')]

def check(N):
    corr = set([ tuple(int(a) for a in e.split(',')) for e in l][:N])

    start = (0,0)
    target = (70, 70)
    op = [start]
    visited = set([])
    dist = {}
    dist[start] = 0

    '''
    for y in range(71):
        s = ''
        for x in range(71):
            if (x,y) in corr:
                s += '#'
            else:
                s += '.'
        print(s)
    '''

    while len(op) > 0:
        this = op.pop(0)
        x,y = this
        d = dist[this]
        for dx,dy in [(1,0), (0,-1), (-1,0), (0,1)]:
            nx,ny = x+dx, y+dy
            if not(0<=nx<=70 and 0<=ny<=70):
                continue
            if (nx, ny) in corr:
                continue
            if (nx,ny) in dist:
                continue
            op.append((nx, ny))
            dist[(nx, ny)] = d+1
    return (70,70) in dist

mn = 1024
mx = len(l)

while mx-mn > 2:
    m = (mx+mn)//2
    t = check(m)
    print(t, m)
    if t:
        mn = m
    else:
        mx = m

for x in range(mn+1, mx):
    t = check(x)
    print(t, x)
    if not t:
        print(str(l[x-1]).replace(' ',''))
