#!/usr/bin/env python3
from math import *
import matplotlib.pyplot as plt
'''
MA305 - Dec. 12th - Kim George!
PURPOSE - Machin's Formula Calculation of Pi
'''

def machine(x,N):
	summa = 0
	for l in range(1,N):
		varia = 2*l - 1
		summa += ((-1)**(l+1))*(1/((x**varia)*(varia)))
	return summa

I = pi
x = []
y = []
k = 0

for i in range(5,m+1):
	machpi1 = (16*machine(5,i))
	machpi2 = (4*machine(239,i))
	T = machpi1 - machpi2
	error = abs((T-I)/I)
	x.insert(k,2**i)
	y.insert(k,error)
	
fig=plt.figure()
plt.plot(x,y,'o')
#plt.legend(['data', 'line of best fit'], loc='best')
plt.title('Machin's Pi error with respect to N')
plt.xlabel('$N$')
plt.ylabel('$Error$')
plt.show()
#plt.figure().savefig('machinPiGraph.png')