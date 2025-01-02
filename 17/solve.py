'''
Target: 2,4,1,5,7,5,1,6,4,3,5,5,0,3,3,0

B := A % 8
B ^= 5
C := A // pow(B)
B ^= 6
B := B ^ C
=== out B ===
A := A // pow(3)
jnz A -> 0
'''

def pb3(x):
	o = ''
	while x:
		o = str(x%8) + o
		x //= 8
	return o

target = [2,4,1,5,7,5,1,6,4,3,5,5,0,3,3,0]

def rek(AA, i):
	if i < 0:
		print(AA)
		raise SystemExit
		return
	t = target[i]
	#print(AA, i)
	m = pow(8, i)
	for a in range(8):
		A = (AA + m*a)//m
		B = A % 8
		B ^= 5
		C = A // pow(2, B)
		B ^= 6
		B ^= C
		if B%8 == t:
			rek(AA+m*a, i-1)

rek(0, len(target)-1)
