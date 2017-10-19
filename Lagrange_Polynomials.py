import numpy as np
import matplotlib.pyplot as plt

def lagrange_polynomial(x, data):

	'''Returns the lagrange polynomial P(x) for a given x and a data set in the form of a list of tuples'''

	n = len(data)
	outer_terms = 0

	for i in range(n):
		inner_terms = data[i][1]
		for j in range(n):
			if (j!=i):
				inner_terms *= (x-data[j][0])/(data[i][0]-data[j][0]) #Computes each term in the polynomial
		
		outer_terms += inner_terms #Sums over the terms

	return outer_terms


########################
#Sampled Function      #
########################
x = np.linspace(-2*np.pi,2*np.pi,10) #Define range for sampled function
#y = np.exp(-x**2)#Define sampled function
y = np.sin(x)

def f(x):
	if (3.<=x<=4.):
		return 3
	else:
		return sin(x)


data = zip(x,y) #Concatenates into a data set

#data = zip(x,f(x))

########################
#Lagrange Polynomial   #
########################
poly_x = np.linspace(-2*np.pi,2*np.pi,100) #Define range for Lagrange Polynomial

fig = plt.figure()
ax = fig.add_axes([0.1,0.1,0.8,0.8])
ax.plot(x,y, marker='o' ,label = 'Sampled function, n = %d' % len(data)) #Plots the original sampled function
ax.plot(poly_x, lagrange_polynomial(poly_x,data), label= 'Lagrange polynomial') #Plots the corresponding lagrange polynomial over the top
ax.grid()
ax.legend(loc='best')
plt.show()