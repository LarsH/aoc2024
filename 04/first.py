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
for x in range(X):
    for y in range(Y):
        for dx,dy in [(1,0), (0,-1), (-1,0), (0,1)]+ [(1,1), (1,-1), (-1,-1), (-1,1)]:
            for i,c in enumerate('XMAS'):
                nx = x+dx*i
                ny = y+dy*i
                if not(0<=nx<X) or not(0<=ny<Y):
                    break
                if l[ny][nx] != c:
                    break
            else:
                o += 1
print(o)
