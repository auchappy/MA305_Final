#!/usr/bin/env python3
from math import *
import matplotlib.pyplot as plt
'''
MA305 - Dec. 12th - Kim George!
PURPOSE - Sum of Alternating series
'''

def arctan(x,N):
	sumalt = 0
	for k in range(1,N):
		vari = 2*k - 1
		sumalt += ((-1)**(k+1))*((x**vari)/(vari))
	return sumalt

m = int(input('Please enter m, where i = 2^m:'))
x =[]
y =[]
k = 0
I = pi


for i in range(5,m+1):
	T = 4 * (arctan(1,i))
	error = abs((T-I)/I)
	x.insert(k,2**i)
	y.insert(k,error)	
	
fig=plt.figure()
plt.plot(x,y,'o')
#plt.legend(['data', 'line of best fit'], loc='best')
plt.title('Alternating sum error with respect to N')
plt.xlabel('$N$')
plt.ylabel('$Error$')
plt.show()
#plt.figure().savefig('altSumPiGraph.png')