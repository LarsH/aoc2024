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
        mn = i//2
    else:
        w += [None]*p

w += [None]

i,j = 0, len(w)-1
mn = mn+1
minfree = 0
while True:
    print(mn)
    mn -= 1
    if mn < 0:
        break
    while j > 0 and not (w[j] == mn and w[j-1] != mn):
        j -= 1

    for s in range(11):
        if w[j+s] != mn:
            break
    else:
        assert False

    #print(f'block {mn} @ {j} has size {s}')

    canmove = False
    i = minfree
    while i < j and not canmove:
        if w[i] != None:
            if i == minfree:
                minfree += 1
            i += 1
        else:
            for q in range(s):
                if w[i+q] != None:
                    i += q
                    break
            else:
                canmove = True
                break
    if not canmove:
        continue
    #print(f'can move to {i}')

    w[i:i+s],w[j:j+s] = w[j:j+s],w[i:i+s]
    #print(''.join(e == None and '.' or str(e) for e in w))

o = 0
for i, n in enumerate(w):
    if n == None:
        continue
    o += i*n
print(o)
