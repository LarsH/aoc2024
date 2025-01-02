# vim: ts=4 sw=4 et sts=-1
from itertools import count
from functools import lru_cache as lru, cmp_to_key
b = '''
2333133121414131402
'''
b = open('input.txt').read()
b = b.strip()

l = [int(e) for e in b]

w = []
for i,p in enumerate(l):
    if i % 2 == 0:
        w += [i//2]*p
    else:
        w += [None]*p
i,j = 0, len(w)-1

while True:
    while w[i] != None and i < j:
        i += 1
    while w[j] == None and j > i:
        j -= 1
    if not (i<j):
        break
    w[i],w[j] = w[j],w[i]

o = 0
for i, n in enumerate(w):
    if n == None:
        break
    o += i*n
print(o)
