# vim: ts=4 sw=4 et sts=-1
from itertools import count
from functools import lru_cache as lru, cmp_to_key
import re

b = '''
xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))
'''
b = open('input.txt').read()
b = b.strip()

l = re.findall(r"mul\((\d+),(\d+)\)", b)
o = 0
for a,b in l:
    t =  int(a)*int(b)
    print(t)
    o += t
print(o)
