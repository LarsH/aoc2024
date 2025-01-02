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
        w.append((i//2, p))
        mn = i//2
    else:
        w.append((None, p))

w.append((None, 0))

mn = mn +1
i,j = 0,len(w)-1
while mn > 0:
    mn -= 1
    while w[j][0] != mn:
        j -= 1
    assert j >= 0

    i = 0
    while i<j:
        if w[i][0] != None:
            i += 1
            continue

        if w[i][1] >= w[j][1]:
            break
        i += 1

    assert w[j][0] == mn
    if (w[i][1] < w[j][1]) or (w[i][0] != None):
        continue

    print('moving', mn, 'from', j, 'to', i)

    s = w[j][1]
    s2 = w[i][1]

    jju = j+1
    jjl = j
    js = s
    if w[j+1][0] == None:
        jju += 1
        js += w[j+1][1]
    if w[j+1][0] == None:
        jjl -= 1
        js += w[j+1][1]
    w = w[:jjl] + [(None, js)] + w[jju:]

    if s == s2:
        w = w[:i] + [(mn, s)]  + w[i+1:]
    else:
        w = w[:i] + [(mn, s), (None, s2-s)] + w[i+1:]
    j = min(j+3, len(w)-1)

o = 0
i = 0
for t,n in w:
    if t == None:
        pass
    else:
        for q in range(n):
            o += t*(i+q)
    i += n

print(o)
# 50323502956580 is wrong
