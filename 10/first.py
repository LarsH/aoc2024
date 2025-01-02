# vim: ts=4 sw=4 et sts=-1
from itertools import count
from functools import lru_cache as lru, cmp_to_key
b = '''
...0...
...1...
...2...
6543456
7.....7
8.....8
9.....9
'''

b2 = '''
..90..9
...1.98
...2..7
6543456
765.987
876....
987....
'''

b3 = '''
89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732
'''
b4= '''
10..9..
2...8..
3...7..
4567654
...8..3
...9..2
.....01
'''

b = b3

b = open('input.txt').read()
b = b.strip()


l = [e for e in b.split('\n')]

l = [[t == '.' or int(t) for t in e]      for e in l]

X = len(l[0])-1
Y = len(l)-1

print(X,Y)
print('===')

def rek(x,y,n):
    if n == 9:
        return set([(x,y)])
        '''
        if (x == 0 or x == X) and (y==0 or y==Y):
            return 1
        else:
            return 0
        '''
    retval = set([])
    for dx,dy in [(1,0), (0,-1), (-1,0), (0,1)]:
        nx,ny = x+dx, y+dy
        if not((0<=nx<=X) and (0<=ny<=Y)):
            continue
        if l[ny][nx] == (n+1):
            retval |= rek(nx, ny, n+1)
    if n == 0:
        #print(x,y, retval)
        return len(set(retval))
    return retval

o = 0
'''
for x in range(X+1):
    if l[0][x] == 0:
        print(x,0)
        o += rek(x,0,0)

for y in range(1,Y):
    if l[y][0] == 0:
        print(0,y)
        o += rek(0,y,0)
    if l[y][X] == 0:
        print(X,y)
        o += rek(X,y,0)

for x in range(X+1):
    if l[Y][x] == 0:
        print(x, Y)
        o += rek(x,Y,0)
'''
for x in range(X+1):
    for y in range(Y+1):
        if l[y][x] == 0:
            #print(x, y)
            o += rek(x,y,0)

print('===')
print(o)
