import numpy as np
import matplotlib.pyplot as plt

dt = 0.1 #time interval
t = np.arange(0,10+dt,dt) #time steps
N = len(t) #no of time steps
dw = (2*np.pi)/(N*dt) #frequency interval
noise = np.random.normal(0,0.2,len(t)) #noise generation 

def dft(f,p):
	'''Returns the DFT for point p for a given function and time series'''
	sum = 0.0j

	for n in range(N): 
		sum+=f[n]*np.exp(1j*p*dw*n*dt)

	return sum

def idft(ftilde,n):
	'''Returns the inverse DFT for point p for a given function and frequency series'''
	sum = 0.0j

	for p in range(N): 
		sum+=ftilde[p]*np.exp(-1j*p*dw*n*dt)

	return sum/N


def f(t):
	'''Defines a function to be decomposed'''
	return np.sin(2*t)+np.cos(10*t)

tseries = f(t)+noise #adds noise to function

wseries = [dft(tseries,p) for p in range(N)]
wseriesreal = [dft(tseries,p).real for p in range(N)]
wseriesimag = [dft(tseries,p).imag for p in range(N)]

invwseriesreal = [idft(wseries,n).real for n in range(N)]

#################################
###PLOTTING######################
#################################

fig1 = plt.figure()
ax1 = fig1.add_axes([0.1,0.1,0.8,0.8])
fig2 = plt.figure()
ax2 = fig2.add_axes([0.1,0.1,0.8,0.8])
fig3 = plt.figure()
ax3 = fig3.add_axes([0.1,0.1,0.8,0.8])
fig4 = plt.figure()
ax4 = fig4.add_axes([0.1,0.1,0.8,0.8])

ax1.plot(t,tseries,marker='o', linestyle='-', alpha=1., markerfacecolor='red' ,color='blue')
ax2.plot(range(-N/2,N/2), wseriesreal, marker='o', linestyle='-', alpha=1., markerfacecolor='red' ,color='blue')
ax3.plot(range(-N/2,N/2), wseriesimag, marker='o', linestyle='-', alpha=1., markerfacecolor='red' ,color='blue')
ax4.plot(t, invwseriesreal, marker='o', linestyle='-', alpha=1., markerfacecolor='red' ,color='blue')
plt.show()

