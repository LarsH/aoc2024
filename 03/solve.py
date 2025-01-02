# vim: ts=4 sw=4 et sts=-1
from itertools import count
from functools import lru_cache as lru, cmp_to_key
import re

b = '''
xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))
'''
b = open('input.txt').read()
b = b.strip()
print(b)

l = re.findall(r"mul\((\d+),(\d+)\)|(do\(\))|(don't\(\))", b)
o = 0
en = True
for a,b,c,d in l:
    print(a,b,c,d)
    if len(a):
        if en:
            o += int(a)*int(b)
        else:
            print('skip')
    elif c == 'do()':
        en = True
    elif d == "don't()":
        en = False
print(o)
