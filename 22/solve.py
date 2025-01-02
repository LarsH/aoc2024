# vim: ts=4 sw=4 et sts=-1
from itertools import count
from functools import lru_cache as lru, cmp_to_key
b = '''
1
2
3
2024
'''
b = open('input.txt').read()
b = b.strip()


l = [e for e in b.split('\n')]

l = [  int(  e )       for e in l]


def round(x):
    x = x ^ (x*64)
    x %= 16777216
    x = x ^ (x//32)
    x %= 16777216
    x = x ^ (x*2048)
    x %= 16777216
    return x

dl = []
for x in l:
    p = float('nan')
    cl = []
    dic = {}
    for i in range(2000):
        pp = p
        x = round(x)
        p = x%10
        diff = p - pp
        if diff is not float('nan'):
            cl = (cl + [diff])[-4:]
        if len(cl) == 4:
            t = tuple(cl)
            if not t in dic:
                dic[t] = p
    dl.append(dic)

s = set([])
for k in dl:
    s |= k.keys()

m = (0, (0,0,0,0))
for k in s:
    #print(k)
    x = sum(e.get(k,0) for e in dl)
    t = (x,k)
    #print(m, t)
    m = max(m,t)
print(m[0])

