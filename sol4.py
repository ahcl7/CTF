import hashlib
file = "/home/ahcl/Desktop/b.txt"
f = open(file, "r")
content = f.read()
f.close()
def redo(s):
    ans = ''
    for c in s:
        if (c!='\n'):
            ans+=c
    return ans
f = open(file, "w")
f.write(redo(content))
f.close()