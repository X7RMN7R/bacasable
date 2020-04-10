import matplotlib.pyplot as plt
import numpy as np
import mandelbrot as mb

size = 300
rangeX = np.linspace(-2,0.5,size)
rangeY = np.linspace(-1.5,1.5,size)

resX = []
resY = []

def showPoint(x, y):
	z = (x,y)
	nthElement = mb.mandelbrot(z, 50)
	return mb.zdist(nthElement) < 4
	
for x in rangeX:
	for y in rangeY:
		if showPoint(x,y):
			resX.append(x)
			resY.append(y)

plt.scatter(resX,resY,1)

plt.xlabel('x - axis')
plt.ylabel('y - axis')

plt.title('Ensemble de Mandelbrot')

plt.show()
