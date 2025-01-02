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



for i in range(101*103):
    ep = set([])

    for r in l:
        (px,py), (vx,vy) = r
        nx = (px + vx*i)%X
        ny = (py + vy*i)%Y
        if nx == X//2:
            continue
        if ny == Y//2:
            continue
        ep.add((nx, ny))

    if (i-240) % 101:
        continue

    print('==='*4)
    print(i)

    for y in range(Y):
        s = ''
        for x in range(X):
            if(x,y) in ep:
                s += '#'
            else:
                s += '.'
        print(s)
