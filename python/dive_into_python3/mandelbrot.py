def zadd(z1, z2):
	return (z1[0] + z2[0], z1[1] + z2[1])
	
def zmult(z1, z2):
	return (z1[0]*z2[0] - z1[1]*z2[1], z1[0]*z2[1] + z1[1]*z2[0])
	
def zsquare(z):
	return zmult(z, z)

def zdist(z):
	return z[0]*z[0] + z[1]*z[1]
	
def mandelbrot(c,n):
	if n == 0:
		return (0, 0)
	else:
		return zadd(zsquare(mandelbrot(c,n-1)), c)

