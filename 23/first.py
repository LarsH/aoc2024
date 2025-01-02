# vim: ts=4 sw=4 et sts=-1
from itertools import count
from functools import lru_cache as lru, cmp_to_key
b = '''
kh-tc
qp-kh
de-cg
ka-co
yn-aq
qp-ub
cg-tb
vc-aq
tb-ka
wh-tc
yn-cg
kh-ub
ta-co
de-co
tc-td
tb-wq
wh-td
ta-ka
td-qp
aq-cg
wq-ub
ub-vc
de-ta
wq-aq
wq-vc
wh-yn
ka-de
kh-ta
co-tc
wh-qp
tb-vc
td-yn
'''
b = open('input.txt').read()
b = b.strip()


l = [e for e in b.split('\n')]

l = [    e.split('-')        for e in l]

conns = {}
for a,b in l:
    if not a in conns:
        conns[a] = set([])
    if not b in conns:
        conns[b] = set([])
    conns[a].add(b)
    conns[b].add(a)

sets = set([])
for a in conns:
    if not a.startswith('t'):
        continue
    for b in conns[a]:
        for c in conns[b] & conns[a]:
            sets.add(tuple(sorted((a,b,c))))
print(len(sets))
