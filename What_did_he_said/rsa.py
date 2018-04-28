
def extended_euclidean(a,b):
    p0 = 1;
    p1 = 0;
    tmp = b
    while (b>0):
        t = a // b
        p2 = (p0 - t * p1) % tmp 
        p0 = p1
        p1 = p2
        c = a % b
        a = b
        b = c
    return p0


def hextochar(x):
    if (x==0): return ''
    else:
        return hextochar(x // 256) + chr(x % 256);

def dectochar(x):
    if (x==0): return ''
    else:
        if (x%100 >=5):
            return dectochar(x // 100) + chr(x % 100 - 5);
        return dectochar(x // 100)

def chartohex(s):
    n = len(s)
    ans = 0
    for i in range(n):
        ans = ans * 256 + ord(s[i])
    return ans

def rsa(p,q,e,c):
    N = p * q
    phi = (p-1) * (q-1)
    d = extended_euclidean(e, phi)
    #print (d * e % phi)
    m = pow(c, d ,N)
    return m
    #return dectochar(m)
    #return m