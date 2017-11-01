import numpy as np
import matplotlib.pyplot as plt

def FFT(f): #f is an array points to be fft'd
	print 'FFT has been called with: ', f
	N = len(f) #takes the number of elements in input array
	
	if(N==1):
		print 'trivial case'
		return f #in the trivial case, the ft of a single element array is just the array itself. 

	#recursive calls
	else:
		print 'take the evens'
		farray_even = FFT(f[0::2]) #carries out the swapping process for the even indices. 
		#NOTE: this runs recursively until all of the even terms in the original series have been split down to 1 term which then triggers the 1st if clause.
		print 'take the odds'
		farray_odd = FFT(f[1::2]) #carries out the swapping process for the odd indices
		farray = [0]*N

		print 'Number of elements in array ', N
		for i in range(0,N/2):
			print 'Taking', farray_even, 'and', farray_odd, 'and multiplying by exponential factor to fill 1st half of array'
			farray[i] = farray_even[i]+np.exp(1j*2*np.pi*i/N)*farray_odd[i]
			print 'Taking', farray_even, 'and', farray_odd, 'and multiplying by exponential factor to fill 2nd half of array'
			farray[i+N/2] = farray_even[i]-np.exp(1j*2*np.pi*i/N)*farray_odd[i]
			print 'Filled array is: ', farray
		return farray


def factorial(n): 
	print 'Factorial has been called with n =', n
	if(n==1):
		return 1
	else: 
		return n*factorial(n-1)

x = np.linspace(0,10,2**2)
#x = np.random.random(1024)

y = np.sin(3*x)+np.cos(4*x)
FFT(y)
#plt.plot(range(len(x)),yfft)
plt.show()
#N = len(y)
#print(len(y))
#(y[1::2][10])
#print(x,y)


