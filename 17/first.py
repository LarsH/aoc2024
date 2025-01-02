# vim: ts=4 sw=4 et sts=-1
from itertools import count
from functools import lru_cache as lru, cmp_to_key
b = '''
Register A: 729
Register B: 0
Register C: 0

Program: 0,1,5,4,3,0
'''
b ='''
A: 2024
B: 0
C: 0

Program: 0,1,5,4,3,0
'''
b = open('input.txt').read()
b = b.strip()
r,p = b.split('\n\n')

rl = [int(e.split()[-1]) for e in r.split('\n')]
pl = [int(e) for e in p.split()[1].split(',')]

def op():
    ins = pl[ip+1]
    if ins == 0:
        return 0
    elif ins == 1:
        return 1
    elif ins == 2:
        return 2
    elif ins == 3:
        return 3
    elif ins == 4:
        return rl[0]
    elif ins == 5:
        return rl[1]
    elif ins == 6:
        return rl[2]
    else:
        assert False, f'invalid op {ins=} {ip=}'

pd = print

ol = []
ip = 0
while ip < len(pl):
    ins = pl[ip]
    ov = pl[ip+1]
    print(f'{ip=} {ins=} {ov=} {op()=} {rl}')

    if ins == 0:
        pd('adv')
        rl[0] = rl[0] //  pow(2, op())

    elif ins == 1:
        pd('bxl')
        rl[1] ^= ov

    elif ins == 2:
        pd('bst')
        rl[1] = op()%8

    elif ins == 3:
        pd('jnz')
        if(rl[0]):
            ip = op()
            continue

    elif ins == 4:
        pd('bxc')
        rl[1] = rl[1] ^ rl[2]

    elif ins == 5:
        pd('=== out ===')
        ol.append(op()%8)

    elif ins == 6:
        pd('bdv')
        rl[1] = rl[0] // pow(2, op())

    elif ins == 7:
        pd('cdv')
        rl[2] = rl[0] // pow(2, op())

    else:
        assert False, f'invalid {ins=} {ip=}'
    ip += 2
print(ip)

print(ol)
print(','.join(str(e) for e in ol))
