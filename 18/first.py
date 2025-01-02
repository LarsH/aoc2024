# vim: ts=4 sw=4 et sts=-1
from itertools import count
from functools import lru_cache as lru, cmp_to_key
b = '''
'''
b = open('input.txt').read()
b = b.strip()


l = [e for e in b.split('\n')]

corr = set([ tuple(int(a) for a in e.split(',')) for e in l][:1024])


start = (0,0)
target = (70, 70)
op = [start]
visited = set([])
dist = {}
dist[start] = 0

for y in range(71):
    s = ''
    for x in range(71):
        if (x,y) in corr:
            s += '#'
        else:
            s += '.'
    print(s)

while len(op) > 0:
    this = op.pop(0)
    x,y = this
    d = dist[this]
    for dx,dy in [(1,0), (0,-1), (-1,0), (0,1)]:
        nx,ny = x+dx, y+dy
        print(nx, ny)
        if not(0<=nx<=70 and 0<=ny<=70):
            print('outside')
            continue
        if (nx, ny) in corr:
            print('blocked')
            continue
        if (nx,ny) in dist:
            print('already')
            continue
        op.append((nx, ny))
        dist[(nx, ny)] = d+1

print(dist[(70, 70)])
