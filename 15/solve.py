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
b3 = '''
#######
#...#.#
#.....#
#..OO@#
#..O..#
#.....#
#######

<vv<<^^<<^^
'''

b = open('input.txt').read()
b = b.strip()
mp,mv = b.split('\n\n')

mp = mp.replace('#','##').replace('O','[]').replace('.','..').replace('@','@.')

l = [e for e in mp.split('\n')]
l = [   list( e)        for e in l]
mv = mv.replace('\n','')

for y, r in enumerate(l):
    for x,c in enumerate(r):
        if c == '@':
            sx,sy = x, y

lut = {'>': (1,0), '^':(0,-1), '<':(-1,0), 'v':(0,1)}

def rek(x,y,dx,dy):
    assert dy == 0
    nx,ny = x+dx, y+dy
    if l[ny][nx] == '#':
        return False
    if l[ny][nx] == '.' or rek(nx, ny, dx, dy):
        l[ny][nx] = l[y][x]
        return True
    else:
        return False

def rekv(xl,y,dy,justCheck=True):
    ny = y+dy
    nxl = xl.copy()

    for nx in xl:
        if l[ny][nx] == '#':
            return False
        if l[ny][nx] == '[':
            assert l[ny][nx+1] == ']'
            nxl.add(nx+1)
        if l[ny][nx] == ']':
            assert l[ny][nx-1] == '['
            nxl.add(nx-1)

    if any(l[ny][nx] == '#' for nx in nxl):
        return False
    tmp = set(nx for nx in nxl if l[ny][nx] != '.')
    if all(l[ny][nx] == '.' for nx in nxl) or rekv(tmp, ny, dy, justCheck):
        if justCheck:
            pass
        else:
            for nx in nxl:
                if not nx in xl:
                    # must be in xl, otherwise space
                    c = '.'
                else:
                    c = l[y][nx]
                l[ny][nx] = c
        return True
    else:
        return False

x, y = sx, sy
for m in mv:
    dx,dy = lut[m]
    if dy == 0:
        if rek(x,y,dx,dy):
            l[y][x] = '.'
            x,y = x+dx, y+dy
    else:
        if rekv(set([x]), y, dy, True):
            rekv(set([x]), y, dy, False)
            l[y][x] = '.'
            x,y = x+dx, y+dy
    '''
    print(m, dx, dy)
    for r in l:
        print(''.join(r))
    '''

o = 0
for y, r in enumerate(l):
    for x,c in enumerate(r):
        if c == '[':
            o += x+ y*100

print(o)
