f = open("some_numbers.txt", "r")
s = f.read()
f.close()

s1 = s.split("\n")
print(s1)
res = 0
for i in range(len(s1)):
	res += int(s1[i])
print(res)