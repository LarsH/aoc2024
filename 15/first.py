# vim: ts=4 sw=4 et sts=-1
from itertools import count
from functools import lru_cache as lru, cmp_to_key
b = '''
##########
#..O..O.O#
#......O.#
#.OO..O.O#
#..O@..O.#
#O#..O...#
#O..O..O.#
#.OO.O.OO#
#....O...#
##########

<vv>^<v^>v>^vv^v>v<>v^v<v<^vv<<<^><<><>>v<vvv<>^v^>^<<<><<v<<<v^vv^v>^
vvv<<^>^v^^><<>>><>^<<><^vv^^<>vvv<>><^^v>^>vv<>v<<<<v<^v>^<^^>>>^<v<v
><>vv>v^v^<>><>>>><^^>vv>v<^^^>>v^v^<^^>v^^>v^<^v>v<>>v^v^<v>v^^<^^vv<
<<v<^>>^^^^>>>v^<>vvv^><v<<<>^^^vv^<vvv>^>v<^^^^v<>^>vvvv><>>v^<<^^^^^
^><^><>>><>^^<<^^v>>><^<v>^<vv>>v>>>^v><>^v><<<<v>>v<v<v>vvv>^<><<>^><
^>><>^v<><^vvv<^^<><v<<<<<><^v<<<><<<^^<v<^^^><^>>^<v^><<<^>>^v<v^v<v^
>^>>^v>vv>^<<^v<>><<><<v<<v><>v<^vv<<<>^^v^>^^>>><<^v>>v^v><^^>>^<>vv^
<><^^>^^^<><vvvvv^v<v<<>^v<v>v<<^><<><<><<<^^<<<^<<>><<><^^^>^^<>^>v<>
^^>vv<^v^v<vv>^<><v<^v>^^^>>>^^vvv^>vvv<>>>^<^>>>>>^<<^v>^vvv<>^<><<v>
v^^>>><<^^<>>^v^<v^vv<>v^<<>^<^v^v><^<<<><<^<v><v<>vv>>v><v^<vv<>v^<<^
'''
b2 = '''
########
#..O.O.#
##@.O..#
#...O..#
#.#.O..#
#...O..#
#......#
########

<^^>>>vv<v>>v<<
'''

b = open('input.txt').read()
b = b.strip()
mp,mv = b.split('\n\n')

l = [e for e in mp.split('\n')]
l = [   list( e)        for e in l]
mv = mv.replace('\n','')

for y, r in enumerate(l):
    for x,c in enumerate(r):
        if c == '@':
            sx,sy = x, y

lut = {'>': (1,0), '^':(0,-1), '<':(-1,0), 'v':(0,1)}

def rek(x,y,dx,dy):
    nx,ny = x+dx, y+dy
    if l[ny][nx] == '#':
        return False
    if l[ny][nx] == '.' or rek(nx, ny, dx, dy):
        l[ny][nx] = l[y][x]
        return True
    else:
        return False

x, y = sx, sy
for m in mv:
    dx,dy = lut[m]
    #print(m, dx, dy)
    if rek(x,y,dx,dy):
        l[y][x] = '.'
        x,y = x+dx, y+dy

for r in l:
    print(''.join(r))

o = 0
for y, r in enumerate(l):
    for x,c in enumerate(r):
        if c == 'O':
            o += x+ y*100

print(o)
