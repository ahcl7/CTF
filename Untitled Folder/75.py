import binascii
cnt = 0
res = [0] * 10000
s = 'GIGEM{'
cnt1 = 0
k = 16
t = '51423167336c344235757a506a6a4434'
t = int(t , 16)
with open("hexxy", "rb") as f:
    byte = 'a'
    while byte != b'':
        # Do stuff with byte.
        byte = ""
        byte = f.read(1)
        if (byte==b''):
        	break
        res[cnt1] = res[cnt1] * 256 + (list(byte))[0]
        
        #print(list(byte)[0])
        cnt+=1
        cnt %= k
        if (cnt==0):
        	cnt1+=1
for i in range(cnt1):
	try:
		print (binascii.unhexlify(hex(res[i] ^ t)[2:]))
	except:
		print('odd')
