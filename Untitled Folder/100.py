from enigma.machine import EnigmaMachine
from enigma.rotors.rotor import Rotor

from enigma.plugboard import Plugboard
import itertools
# setup machine according to specs from a daily key sheet:


machine = EnigmaMachine.from_key_sheet(
   rotors='I II III',
   reflector='B',
   ring_settings=[15, 15, 15],
   plugboard_settings='AV BS CG DL FU HZ IN KM OW RX')
pt = 'YRUHQSLDPXNGOKMIEBFZCWVJAT'
machine.reflector = Rotor('my reflector', pt)
machine.set_display('HYM')
s = 'IPUXZGICZWASMJFGLFVIHCAYEGT'
h = 'IPUXZGICZDJOKZUOSDCVHCAYEGT'
f = 'HOWDYAGGIESTHEWEATHERISFINE'
#print (s)
def process(pos, s):
	machine.set_display(pos)
	print(machine.process_text(s))

process("YDM", f)
#c = machine.process_text('HOWDYAGGIESTHEWEATHERISFINE')
#print(c)
# set machine initial starting position

def match(s,s1):
	ans = sum(1 if (a==b) else 0 for a,b in zip(s,s1))
	return ans
def find():
	for i in range(26):
		machine.set_display("HYM")
		tmp = list(pt)
		tmp1 = tmp[i]
		tmp[i] = chr(65 + i)
		tmp[ord(tmp1)-65] = tmp1
		tmp = "".join(tmp)
		#print(tmp)
		machine.reflector = Rotor("my reflector", tmp)
		c1 = machine.process_text(f)
		if (match(c1,s)>=16):
			print(match(c1,s))
			print(tmp[i], tmp1)
			print(c1)
#find()

def pertofind():
	t = list(itertools.permutations(['B','R','F','S','I','P','M','O']))
	n = len(t)
	for i in range(n):
		tmp = list(pt)
		for j in range(4):
			c = t[i][j*2]
			c1 = t[i][j*2+1]
			tmp[ord(c)-65] = c1
			tmp[ord(c1)-65] = c
		tmp = "".join(tmp)
		machine.set_display("HYM")
		machine.reflector = Rotor("my reflector", tmp)
		c1 = machine.process_text(f)
		if (match(c1,s)>17):
			print(match(c1,s))
			print (tmp)
			print(c1)

#pertofind()
f = 'LTHCHHBUZODFLJOAFNNAEONXPLDJQVJCZPGAVOLN'
s = 'PASSWORD'
t = range(ord('A'), ord('Z') + 1)
for i in t:
	for j in t:
		for k in t:
			init = chr(i) + chr(j) + chr(k)
			machine.set_display(init)
			c1 = machine.process_text(f)
			
			if (c1[:4] == s[:4]):
				print(init)
				print(c1)
				print(match(s,c1))
print(s)

#machine.set_display('WNB')
machine.process_text('LTHCHHBUZODFLJOAFNNAEONXPLDJQVJCZPGAVOLN')

# decrypt the message key
#msg_key = machine.process_text('KCH')

# decrypt the cipher text with the unencrypted message key
#machine.set_display(msg_key)

#ciphertext = 'NIBLFMYMLLUFWCASCSSNVHAZ'
#plaint'LTHCHHBUZODFLJOAFNNAEONXPLDJQVJCZPGAVOLN')
#t = machine.process_text(ciphertext)

#print(plaintext)
