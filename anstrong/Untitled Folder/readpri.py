import base64
import struct
import binascii
f = open("private_key_ex")
s = f.read()
s = s.replace('\n','')
f.close()

print(s)
s = base64.b64decode(s)
parts = []
cnt = 0
while (s):
	cnt = cnt+1
	dlen = struct.unpack('>I', s[:4])[0]
	print(dlen)
	data = s[4:dlen+4]
	s = s[dlen+4:]
	parts.append(int(binascii.hexlify(data),16))
print(parts)
print(cnt)
