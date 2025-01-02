# vim: ts=4 sw=4 et sts=-1
from itertools import count
from functools import lru_cache as lru, cmp_to_key
b = '''
x00: 1
x01: 0
x02: 1
x03: 1
x04: 0
y00: 1
y01: 1
y02: 1
y03: 1
y04: 1

ntg XOR fgs -> mjb
y02 OR x01 -> tnw
kwq OR kpj -> z05
x00 OR x03 -> fst
tgd XOR rvg -> z01
vdt OR tnw -> bfw
bfw AND frj -> z10
ffh OR nrd -> bqk
y00 AND y03 -> djm
y03 OR y00 -> psh
bqk OR frj -> z08
tnw OR fst -> frj
gnj AND tgd -> z11
bfw XOR mjb -> z00
x03 OR x00 -> vdt
gnj AND wpb -> z02
x04 AND y00 -> kjc
djm OR pbm -> qhw
nrd AND vdt -> hwm
kjc AND fst -> rvg
y04 OR y02 -> fgs
y01 AND x02 -> pbm
ntg OR kjc -> kwq
psh XOR fgs -> tgd
qhw XOR tgd -> z09
pbm OR djm -> kpj
x03 XOR y03 -> ffh
x00 XOR y04 -> ntg
bfw OR bqk -> z06
nrd XOR fgs -> wpb
frj XOR qhw -> z04
bqk OR frj -> z07
y03 OR x01 -> nrd
hwm AND bqk -> z03
tgd XOR rvg -> z12
tnw OR pbm -> gnj
'''
b = open('input.txt').read()
b = b.strip()
a,b = b.split('\n\n')


vals = dict(e.split(': ') for e in a.split('\n'))
l = [e.split() for e in b.split('\n')]
ops = {e[-1]:e[:-1] for e in l}

@lru(None)
def val(s):
    if s in vals:
        return int(vals[s])
    else:
        a,op,b,_ = ops[s]
        a = val(a)
        b = val(b)
        if op == 'OR':
            return int(a or b)
        elif op == 'XOR':
            return a ^ b
        elif op == 'AND':
            return int(a and b)
        else:
            assert False, (s, op)

bits = ''
for x in sorted(ops)[::-1]:
    if not x.startswith('z'):
        continue
    bits += str(val(x))
print(int(bits,2))
