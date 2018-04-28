import struct
from binascii import *
f = open("flag.png.enc")
s = f.read()
def extend_euclid(a,b):
	p = 1
	q = 0
	while (b>0):
		t = a // b
		tmp = q
		q = p - t * q
		p = tmp
		c = a%b
		a = b
		b = c
	return p

print(extend_euclid(16,7))
t = s[0:4]
print(t)
def lcg(m, a, c, x):
	return (a*x + c) % m

d = unhexlify('89504e47')
#
x = int('89504e47',16) ^ int(hexlify(s[0:4]),16)
#2445943554
x1 = int('0d0a1a0a', 16) ^ int(hexlify(s[4:8]), 16)

x2 = int('0000000d', 16) ^ int(hexlify(s[8:12]), 16)

x3 = int('49484452', 16) ^ int(hexlify(s[12:16]), 16)
m = pow(2,32)
A = (x-x1) % m
B = (x1-x2) % m
a = (extend_euclid(A,m) * B) % m
c = (x1 - a * x) % m
print (a,c,m)

print(x,x1,x2,x3)

print(x)
rs = struct.pack('>I', x ^ struct.unpack('>I', d)[0])
print (rs, t)
# a = 214013
m = pow(2,32)
c = (x1 - a * x) % m
print c
res = ""
for i in range(0,len(s), 4):
	e = struct.pack('>I', x ^ struct.unpack('>I', s[i:i+4])[0])
	res += e
	x = lcg(m, a, c, x)
	if (i==0):
		print x

f = open("res.png", "w")
f.write(res)
f.close()