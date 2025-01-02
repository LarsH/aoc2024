# vim: ts=4 sw=4 et sts=-1
from itertools import count
from functools import lru_cache as lru, cmp_to_key
b = '''
r, wr, b, g, bwu, rb, gb, br

brwrr
bggr
gbbr
rrbgbr
ubwu
bwurrg
brgr
bbrgwb
'''
b = open('input.txt').read()
b = b.strip()

a,b = b.split('\n\n')

l1 = [e for e in a.replace(',','').split()]
l2 = [e for e in b.split()]

l2 = [(len(e), e) for e in l2]
l2 = [(b) for a,b in sorted(l2)]

@lru(None)
def check(s):
    if s == '':
        return 1
    rv = 0
    for x in l1:
        if s.startswith(x):
            rv += check(s[len(x):])
    return rv

print(sum(check(e) for e in l2))
