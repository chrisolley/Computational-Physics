import numpy as np 
import matplotlib.pyplot as plt
from LUDecomp import lu

def li(data):
	'''Performs a linear interpolation on a set of data points (x,y).'''

	p = 100 # density of interpolation
	N = len(data)

	x = np.linspace(data[0,0], data[-1,0], p*(N-1))

	f = np.zeros((len(x),2))

	for i in range(N-1):
		for j in range(p):
			f[i*p+j,0] = x[i*p+j]
			point = ((data[i+1,0]-x[i*p+j])*data[i,1]+data[i+1,1]*(x[i*p+j]-data[i,0]))/(data[i+1,0]-data[i,0])
			f[i*p+j,1] = point

	return f

def csi(data):
	'''Perfoms a cubic spline interpolation on a set of data points (x,y).'''
	N = len(data)
	#Set up the matrix equation to solve for second derivatives
	d = np.zeros((N-2,1))
	m = np.zeros((N-2,1))
	l = np.zeros((N-2,1))
	M = np.zeros((N-2,N-2))

	#populate the x vector for second derivative solving
	for i in range(1,N-1):
		d[i-1] = ((data[i+1,1]-data[i,1])/(data[i+1,0]-data[i,0]))-((data[i,1]-data[i-1,1])/(data[i,0]-data[i-1,0]))
		m[i-1] = (data[i,0]-data[i-1,0])/6
		l[i-1] = (data[i+1,0]-data[i-1,0])/3
	
	#populate the coefficient matrix for second derivative solving
	for i in range(1,N-3):
		M[i,i-1] = m[i-1]
		M[i,i] = l[i-1]
		M[i,i+1] = m[i]

	M[0,0] = l[0]
	M[0,1] = m[1]
	M[N-3,N-3] = l[N-3]
	M[N-3,N-4] = m[N-3]

	#solve for the second derivatives using lu decomposition algorithm
	f2prime = lu(M,d)
	print N
	print len(f2prime)
	#produce the cubic spline points for each segment
	p = 100 # density of interpolation

	x = np.linspace(data[0,0], data[-1,0], p*(N-1))

	f = np.zeros((len(x),2))

	for i in range(N-1):
		for j in range(p):
			f[i*p+j,0] = x[i*p+j]
			A = (data[i+1,0]-x[i*p+j])/(data[i+1,0]-data[i,0])
			B = 1-A
			C = (1./6.)*(A**3-A)*(data[i+1,0]-data[i,0])**2
			D = (1./6.)*(B**3-B)*(data[i+1,0]-data[i,0])**2

			if (i==0) or (i==N-2):
				point = A*data[i,1]+B*data[i+1,1]
			else:
				point = A*data[i,1]+B*data[i+1,1]+C*f2prime[i-1]+D*f2prime[i]

			f[i*p+j,1] = point

	return f



N = 25
x = np.linspace(0,2*np.pi,N)
# data = np.zeros((N,2))
# for i in range(N):
# 	data[i,0] = x[i]
# 	data[i,1] = np.sin(x[i])+np.exp(-(x[i]-np.pi)**2/0.1)
# 	data[i,1] = np.sin(x[i])+np.exp(-(x[i]-np.pi)**2/0.1)

raw_data = np.array([[-2.1,-1.45,-1.3,-0.2,0.1,0.15,0.8,1.1,1.5,2.8,3.8],[0.012155,0.122151,0.184520,0.960789,0.990050,0.977751,0.527292,0.298197,0.105399,3.93669*10**(-4),5.355348*10**(-7)]])

data = np.zeros((raw_data.shape[1],2))

for i in range((raw_data.shape[1])):
	data[i,0] = raw_data[0,i]
	data[i,1] = raw_data[1,i]

cubic = csi(data)
linear = li(data)
plt.plot(cubic[:,0],cubic[:,1], color = 'blue', label='Cubic Spline')
plt.plot(linear[:,0],linear[:,1], color = 'green', label='Linear Interpolation')
plt.plot(data[:,0], data[:,1], marker='+', linestyle='', color='red',markersize=20, alpha=1.)
plt.legend(loc='best')
plt.grid()
plt.show()