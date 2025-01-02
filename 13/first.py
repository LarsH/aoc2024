# vim: ts=4 sw=4 et sts=-1
from itertools import count
from functools import lru_cache as lru, cmp_to_key
b = '''
Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400

Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=12748, Y=12176

Button A: X+17, Y+86
Button B: X+84, Y+37
Prize: X=7870, Y=6450

Button A: X+69, Y+23
Button B: X+27, Y+71
Prize: X=18641, Y=10279
'''
b = open('input.txt').read()
b = b.strip()


l = [e for e in b.split('\n\n')]

def f(s):
    a,b,c = s.split('\n')
    _,_,x,y = a.split()
    ax = int(x[2:-1])
    ay = int(y[2:])

    _,_,x,y = b.split()
    bx = int(x[2:-1])
    by = int(y[2:])

    _,x,y = c.split()
    cx = int(x[2:-1])
    cy = int(y[2:])

    k = float('inf')
    for a in range(101):
        x = cx - ax*a
        y = cy - ay*a
        if x < 0:
            break
        if y < 0:
            break
        if x % bx != 0:
            continue
        if y % by != 0:
            continue
        if x // bx != y // by:
            continue
        b = x // bx
        k = min(k, 3*a + b)
    if k > 9e99:
        k = 0
    print(k)
    return k


l = [ f(   e )       for e in l]

print(sum(l))
# 23057
