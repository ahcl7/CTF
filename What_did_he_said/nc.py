import socket
import time
#from Crypto.Util.Number import *
def process(s, socket):
    pk = [''] * 3
    res = ''
    if ('Harekaze' not in s):
        #print(s)
        ok = False
        n = len(s)
        cnt = 0
        pos = -1
        for i in range(n):
            if (cnt==3):
                break
            if (s[i] == '('):
                ok = True
                continue
            if (s[i] == ')'):
                cnt += 1
                if (cnt==3):
                    pos = i
                ok = False
            if (ok):
                pk[cnt] += s[i]
        n = [0] * 3
        e = [0] * 3
        c = [0] * 3
        for i in range(3):
            n[i] = int(pk[i].split(',')[0], 16)
            e[i] = int(pk[i].split(',')[1], 10)
            c[i] = int(pk[i].split(',')[2], 16)
            #
            if (pow(6289644257982517902, e[i], n[i]) == c[i]):
                socket.sendall((str(i+1) + '\n').encode())
                print("RES: ",i+1)
        return s[pos+1:]
    else:
        print(s)
def ok(data):
    return data.count(')') >=3
def netcat(hostname, port, content):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((hostname, port))
    #s.sendall(content)
    #s.shutdown(socket.SHUT_WR)
    data = ''
    round = 1
    while 1:
        data += s.recv(1024).decode('utf-8')
        if (round == 31):
            print(data
)        if (ok(data)):
            print("ROUND ", round)
            if data == "":
                break
            #print data
            data = process(data, s)
            round+=1
    print("Connection closed.")
    s.close()

netcat('problem.harekaze.com', 30214, 'asdf')


#HarekazeCTF{92f4187adbbafd3c592bfdfa8689de3be26b770d}