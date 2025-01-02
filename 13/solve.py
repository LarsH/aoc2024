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

import numpy
import fpylll
def reduceLattice(lattice):
    A = fpylll.IntegerMatrix.from_matrix(lattice)
    M = fpylll.GSO.Mat(A)
    M.update_gso()
    L = fpylll.LLL.Reduction(M)
    print('=====')
    print(A)
    print('---')
    L()
    print(A)
    if A[2][0] != 0 or A[2][1] != 0:
        return 0
    assert A[2][2] >= 0 and A[2][3] >= 0
    return A[2][4]



from math import gcd

def f(s):
    a,b,c = s.split('\n')
    _,_,x,y = a.split()
    ax = int(x[2:-1])
    ay = int(y[2:])

    _,_,x,y = b.split()
    bx = int(x[2:-1])
    by = int(y[2:])

    _,x,y = c.split()
    cx = int(x[2:-1])+10000000000000
    cy = int(y[2:]) + 10000000000000

    M = (1<<30)-1
    L = [[cx*M*M, cy*M*M, 0, 0, 0, M*M],
        [-ax*M*M, -ay*M*M, 1, 0, 3*M, 0],
        [-bx*M*M, -by*M*M, 0, 1, M, 0]]

    return reduceLattice(L)//M


l = [ f(   e )       for e in l]

print(sum(l))
# 38980958139391
