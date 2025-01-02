# vim: ts=4 sw=4 et sts=-1
from itertools import count
from functools import lru_cache as lru, cmp_to_key
b = '''
p=0,4 v=3,-3
p=6,3 v=-1,-3
p=10,3 v=-1,2
p=2,0 v=2,-1
p=0,0 v=1,3
p=3,0 v=-2,-2
p=7,6 v=-1,-3
p=3,0 v=-1,-2
p=9,3 v=2,3
p=7,3 v=-1,2
p=2,4 v=2,-3
p=9,5 v=-3,-3
'''
X,Y = (11, 7)
b = open('input.txt').read()
X,Y = (101, 103)
b = b.strip()


l = [e for e in b.split('\n')]

l = [[[int(p) for p in q.split('=')[1].split(',')] for q in   e.split()]        for e in l]


c = [[0,0],[0,0]]
ep = []
for r in l:
    (px,py), (vx,vy) = r
    nx = (px + vx*100)%X
    ny = (py + vy*100)%Y
    if nx == X//2:
        continue
    if ny == Y//2:
        continue
    c[int(nx >X//2)][int(ny > Y//2)] += 1
    ep.append((nx, ny))

'''
for y in range(Y):
    s = ''
    for x in range(X):
        s += str(ep.count((x,y)))
    print(s)
'''

print(c)
# 224160300
