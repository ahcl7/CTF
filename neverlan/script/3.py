f = open("3.txt", "r")
s = f.read()
f.close()
t = 0
res = 0
for i in range(len(s)):
	if (s[i] >= '0' and s[i] <='9'):
		t = t * 10 + ord(s[i]) - 48
	else:
		res += t
		t = 0	
print res