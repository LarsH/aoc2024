# vim: ts=4 sw=4 et sts=-1
from itertools import count
from functools import lru_cache as lru, cmp_to_key
b = '''
47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47
'''
b = open('input.txt').read()
b = b.strip()
b1,b2 = b.split('\n\n')

l = [e.split('|') for e in b1.split('\n')]
l1 = [ (int( a),int(b))        for a,b in l]

l2 = [e.split(',') for e in b2.split('\n')]
l2 = [ [int( a)for a in b]  for b in l2]

def check(x):
    if len(x) <= 1:
        return True
    a,*rest = x
    for p,q in l1:
        if q == a:
            #print(p,q, a, rest)
            for t in rest:
                if t == p:
                    return False
    return check(rest)

assert not check([16, 13, 29])
o = 0
for u in l2:
    if check(u):
        print(u)
        m = u[(len(u))//2]
        print(m)
        o += m
print(o)