# vim: ts=4 sw=4 et sts=-1
from itertools import count
from functools import lru_cache as lru, cmp_to_key
b = '''
MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX
'''
b = open('input.txt').read()
b = b.strip()


l = [e for e in b.split('\n')]
l = [    e        for e in l]

Y = len(l)
X = len(l[0])

o = 0
for x in range(1,X-1):
    for y in range(1,Y-1):
        if not l[y][x] == 'A':
            continue
        q = [(1,1), (1,-1), (-1,-1), (-1,1)]*2
        for i in range(4):
            for c,(dx,dy) in zip('SSMM', q[i:]):
                nx = x + dx
                ny = y + dy
                if l[ny][nx] != c:
                    break
            else:
                o += 1
print(o)
