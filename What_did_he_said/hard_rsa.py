n = 8803019775775360139632158464672610112189698498229081300640697369390018949264336363289492470451786850852762589509561329269405497678684623354691318978632479
e = (1<<16) + 1
c = 3110473700733417399933670089300385183134001510545717948027369708719679400206482152185999271142947549784641693759573980270656066786360866269313311930844499
def gcd(a,b):
	while (b):
		c = a % b
		a = b
		b = c
	return a
def sqrt(x):
	l = 0
	r = x
	ans = -1
	while (l<=r):
		g = (l+r) >> 1
		t = g * g
		if (t == x):
			return True, g
		if (t > x):
			ans = g
			r = g-1
		else:
			l = g+1
	return False, ans

def isSquare(x):
	return sqrt(x)[0]

def fermat_factorize(x):
	a = sqrt(x)[1]
	b = a * a - x
	while (not isSquare(b)):
		a += 1
		b = a * a - x
	return (a + sqrt(b)[1])
def pollard(x):
	a = 2
	i = 1
	while (True):
		a = pow(a, i, x)
		if (gcd(a-1 , x) !=1):
			return gcd(a-1, x)
		i += 1
