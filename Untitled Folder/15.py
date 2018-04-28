import base64
s = 'IFhiPhZNYi0KWiUcCls='
s1 = 'El Psy Congroo'
flag = 'I3gDKVh1Lh4EVyMDBFo='
t = base64.b64decode(s).encode()
f = [101,52,66,110]
for i in range(14):
	print ((ord(t[i]) ^ ord(s1[i])))
flag = base64.b64decode(flag)
fl = ''
for i in range(len(flag)):
	flag += chr(ord(flag[i]) ^ f[i%4])
print(flag)