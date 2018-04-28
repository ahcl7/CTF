from math import sqrt
import base64
N = 0x9cdebcfaae6c9258e6c53b70bc103763b1fbe71c34d2ed33af30abf36686fb6534e9d3c693252e8921f6d2fb8bc6db78fdb6981eab9fb5268e5e12f0647d745d38926c63d6a08d566d2d2d028bbeec830025bf13f8448c68bd0f23c6d8156a7cdec4851cb14f4d784e06bbbc47c740829f35054f573fe772b519bdf625afd45fadcf735cf22ee08594829f7f371252c4723833bb1d0e27e87987994144b2a709ddce504cd4f2f2328d284024ed38b92456addaee2004506539ed0920bcf0beb1a12cdfa986253bc2cf503967985bb658dacf130bccec8bb8656c973f2455ef7301cb33fdd183531fdebcf3eca1bfe9c8c8ae1bbdac3112b80a58000000000001

E = 0x10001

C = 0x8cd7457734ed6337b78c970f831e4a9ac19fb2352ebb11a984f0d5028c5fc041967a1d966bd41b6cab32a45634c7fd64028103466b4c20d121a720cba8ecf0369bc43b8cd8ffa80b92b44091b7a8e6978c773bd0b4029bb20424c16ad563586b8702f5af3efa107cc3425e74cbb9bded983f7d1b90a0b64e7a1293cfd06c864c1c3baec253f504a9b2bed12727d4a3fda1b8563b66ec8b80c603661ff91a27a89475a1eaed5b717afd7e3687aa295a2526200f306b9abf5b5a90afafb61d0d942592b57a88d7366e5931cd277b264b5474202e8a854778ba5b8e86833ccc63e52a41845eec557fb8752bfd6eeec84c19af90baa53bb0b4aa86c2fd81aa6a4563
def nt(x):
    if (x<2): return False;
    if (x==2): return True
    t = sqrt(x)
    for i in range(2,int(t)+1):
        if (x%i==0): return False
    return True
def sqrt(x):
    l = 0
    r = x
    ans = -1
    while (l<=r):
        g = (l+r) // 2
        t = g *g
        if (t == x):
            return g
        if (t <x):
            l = g+1
            ans = g
        if (t >x):
            r = g-1
    return (l+r)//2

def isSquare(x):
    t = sqrt(x)
    return t * t == x

def process():
    return
def solvequaratic(a, b, c, callback):
    delta = b * b - 4 * a * c
    print delta
def fermat_factorization(x):
    a = 0
    if (isSquare(x)):
        a = sqrt(x)
    else:
        a = sqrt(x) + 1
    b = a * a - x
    while (not(isSquare(b)) ):
        a = a + 1
        b = a * a - x
    print a , sqrt(b)
fermat_factorization(N)