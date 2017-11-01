import numpy as np
from Matrix_Operations import rand_mat

#TODO Comments

def entry():
	'''Takes in user entry of a matrix.'''

	dim = input('Enter matrix dimension in form (rows,cols): ')
	a = np.zeros((dim[0],dim[1]))

	for i in range(dim[0]):
		a[i] = input('Enter row {} (comma-separated): '.format(i))
		print 'A: '
		print a
	
	return a

def crout(a):

	'''Carries out LU Decomposition using Crout's algorithm. Returns l, u and det(a).'''

	a_nrows = a.shape[0]
	a_ncols = a.shape[1]

	if(a_ncols!=a_nrows):
		raise Exception('LU Decomposition requires a square matrix')

	N = a_nrows

	l = np.zeros((N,N))
	u = np.zeros((N,N))

	for i in range(N):
		l[i,i]=1.

	for j in range(N): 
		for i in range(j+1):
			if(i==0): 
				sumterm = 0.
			else: 
				sumterm = 0.
				for k in range(i):
					sumterm+=l[i,k]*u[k,j]

			u[i,j] = a[i,j]-sumterm
		
		for i in range(j+1, N):
			if(j==0):
				sumterm = 0.
			else: 
				sumterm = 0.
				for k in range(j):
					sumterm+=l[i,k]*u[k,j]

			l[i,j]=(1./u[j,j])*(a[i,j]-sumterm)

	det = 1

	for i in range(N): 
		det *= u[i,i]

	if(np.allclose(a,np.dot(l,u))!=True):
		print 'Error in decomposition.'

	return l,u,det

def lu(a,b): 

	'''Solves matrix equation using LU decomposition.'''

	N = a.shape[0]
	M = b.shape[1]

	result = crout(a)
	l = result[0]
	u = result[1]

	y = np.zeros((N,M))
	x = np.zeros((N,M))

	
	for k in range(M):

		y[0,k] = b[0,k]/l[0,0]

		for i in range(1,N):
			sumterm = 0
			for j in range(0,i):
				sumterm+=l[i,j]*y[j,k]
			y[i,k] = (1./l[i,i])*(b[i,k]-sumterm)

		x[N-1] = y[N-1]/u[N-1,N-1]

		for i in range(N-2,-1,-1): 
			sumterm = 0
			for j in range(i,N):
				sumterm+=u[i,j]*x[j,k]
			x[i,k] = (1./u[i,i])*(y[i,k]-sumterm)

	if(np.allclose(b,np.dot(a,x))!=True):
		print 'Solution error.'
	return x



def main():

	print 'Solving A.X=B using LU decomposition.'
	print 'A is a matrix and X,B can be matrices in general.'
	q = input('Do you want to solve a matrix equation (1) or find the inverse of a matrix? (2) (Enter 1 or 2): ')

	if (q==1):
		print 'Enter A: '
		a = entry()
		print 'Enter B: '
		b = entry()
		print 'Solving...'
		solution = lu(a,b)
		print 'X: '
		print solution

	if (q==2):
		print 'Enter A: '
		a = entry()
		N = a.shape[0]
		print 'Inverting...'
		solution = lu(a,np.ones((N,N)))
		print 'A^-1: '
		print solution
main()
	
