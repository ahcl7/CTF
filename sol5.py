s='ENDTBTXNYVULWOFKJEGBYSTFPFMJFYMNVCBPYDDFSQOKEGPKX'
dir=[0,0,1,1,1,1,0,
    1,1,1,0,0,1,1,
    0,1,1,1,1,0,1,
    0,1,1,1,0,1,0,
    1,1,0,1,0,1,1,
    0,1,0,1,1,1,1,
    0,1,1,0,1,1,0]
t = 0
res = ''
for i in range(len(dir)):
    t = t + dir[i]
    c = chr((ord(s[i]) - 65 -t + 26) % 26 + 65)
    res += c
print res
