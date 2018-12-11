#!usr/bin/env python3
"""
==============================
Chapman, Piers - 05NOV18
Purpose: Calculate pi using the simpsons rule
==============================
"""
from math import *
import time as clock
import stopwatch as watch

def f(x):
	t = 1-x**2
	return 8*(sqrt(t)-x)

def simpsons(f, a, b, n):
	h = (b - a)/float(n)
	sum1 = 0
	for i in range(1, int(n/2 + 1)):
		sum1 += f(a + (2*i - 1)*h)
	sum2 = 0
	for i in range(1, int(n/2)): 
		sum2 += f(a + 2*i*h)
	approx = (b - a)/(3.0*n)*(f(a) + f(b) + 4*sum1 + 2*sum2)
	return approx
a = 0
b = 1/sqrt(2)
print("  m            N             ~Pi             error      mm:ss:sss")
I = pi

for i in range(2,10):
	start = clock.time()
	T = simpsons(f,a,b,int(2**i))
	end = clock.time()
	error = abs((T-I)/I)
	timeLen = end-start
	mn,sc,ms = watch.stopwatch(timeLen)
	print('{0:3d}\t{1:10.1f}\t{2:10.10f}\t{3:2.10f}\t{4:02}:{5:02}:{6:03}'.format(i,2**i,T,error,mn,sc,ms))

