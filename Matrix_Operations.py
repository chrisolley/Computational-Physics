import matplotlib.pyplot as plt
import numpy as np
import random as random
from timeit import default_timer as timer


def rand_mat(m,n):
	''' Returns a random matrix (integers between 1 and 10) of dim (m,n)'''

	a = np.zeros((m,n))

	for i in range(m):
		for j in range(n):
			a[i,j]=random.randint(1,10)

	return a

def matrix_multiplication(a,b):

	'''Multiplies two matrices if their dimensions are appropriate '''
	print('Multiplying')
	print(a, 'and')
	print(b , '...')

	start = timer()
	a_nrows = a.shape[0]
	a_ncols = a.shape[1]
	b_nrows = b.shape[0]
	b_ncols = b.shape[1]

	if(a_ncols!=b_nrows):
		raise Exception('Matrices cannot be multiplied')

	c = np.zeros((a_nrows,b_ncols))

	for i in range(0,a_nrows):
		for j in range(0,b_ncols):
			c[i,j] = sum([x*y for x,y in zip(a[i,:],b[:,j])]) #Gets required row from a and column from b and sums over product of each element.

	end = timer()

	if(np.allclose(c,np.dot(a,b))==True): # checks result
		print('Matrix multiplication correct. Execution time: %0.3fms.' % ((end-start)*1000))
	else:
		print('Incorrect multiplication. Execution time: %0.3fms.' % ((end-start)*1000))

	return c

def gauss_jordan_solver(a,b): 
	'''Uses Gauss-Jordan Elimination to solve the matrix equation a.x=b for a given matrix a and vector b. No pivoting implemented.'''

	print('-------------------------------------------')
	print('Solving matrix equation of the form a.x=b')
	print('-------------------------------------------')
	a_nrows = a.shape[0]
	a_ncols = a.shape[1]

	if(a_ncols!=a_nrows):
		raise Exception('Matrix must be square')

	print('a matrix: ') 
	print(a)
	print('b vector: ') 
	print  b
	
	a_aug = np.zeros((a_nrows, a_ncols+1)) #instantiates augmented matrix
	m = np.zeros((a_nrows, a_ncols))
	m = a #copy of original coefficient matrix

	for i in range(a_nrows): #populates augmented matrix
		for j in range(a_ncols):
			a_aug[i,j] = a[i,j]
		a_aug[i,a_ncols] = b[i]

	a = a_aug #now working with augmented matrix
	a_nrows = a.shape[0] #sets row/col numbers to augemented matrix
	a_ncols = a.shape[1]

	print('-------------------------------------------')
	print('Carrying out Gauss-Jordan Elimination...')
	print('-------------------------------------------')

	start = timer()
	for k in range(a_ncols-1): #loop over every colum
		diag = a[k,k] #temp variable to hold value of diagonal element in each column
		for i in range(a_nrows): #row operation to obtain diagonal element of each column
			if(i==k): 
				for j in range(a_ncols):
					a[i,j]=a[i,j]/diag
		
		for i in range(a_nrows): #row operation to obtain off-diagonal elements of each column
			temp = a[i,k] #temp variable to hold value of kth column element
			if(i!=k):
				for j in range(a_ncols):
					a[i,j] = a[i,j] - temp*a[k,j]
	end = timer()

	x = np.zeros((a_nrows,1))
	x = a[:,-1].reshape(a_nrows,1)

	if(np.allclose(b,np.dot(m,x))==True):
		print('-------------------------------------------')
		print('Solved. Execution time: %0.3fms.' % ((end-start)*1000))
		print('-------------------------------------------')
	
	print('Diagonalised augmented matrix: ')
	print(a_aug)
	print('Solution vector: ')
	return x 

	#  	else:
	#  		a[i,1] = a[i,1]-a[i,1]*a[1,1]

	#a[0,1] = a[0,1]-a[0,1]*a[1,1]
	#a[2,1] = a[2,1]-a[2,1]*a[1,1]




	# diag = a[1,1] #temp variable to hold value of diagonal element in each column
	# for i in range(0,a_nrows):
	# 	if(i==1):
	# 		for j in range(0,a_ncols):
	# 			a[i,j]=a[i,j]/diag
	# 	else:
	# 		temp = a[i,1] #temp variable to hold value of 0th column element
	# 		for j in range(0,a_ncols):
	# 			a[i,j] = a[i,j] - temp*a[0,j]



a = rand_mat(5,5)
b = rand_mat(5,1)
#print(matrix_multiplication(a,b))

print(gauss_jordan_solver(a,b))