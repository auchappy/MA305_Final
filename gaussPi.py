#!usr/bin/env python3
"""
==============================
Chapman, Piers - 05NOV18
Purpose: Calculate pi using the 2-point gauss rule
==============================
"""
from math import *
import time as clock
import stopwatch as watch

def f(x):
	return 4/(1+x**2)

def gauss(f,a,b,n):
	h = (b-a)/n
	fi = 0.0
	xi = 0.0
	pxi = 0.0
	for i in range (1,n):
		xi = a + i*h
		x2 = (0.5)*(xi+pxi+(h/sqrt(3)))
		x1 = (0.5)*(xi+pxi-(h/sqrt(3)))
		fi += f(x1)+f(x2)
		pxi = xi
	return h*0.5*fi

a = 0
b = 1
m = int(input('Please enter m, where i = 2^m:'))
print("  m            N             ~Pi             error      mm:ss:sss")
I = pi

for i in range(5,m+1):
	start = clock.time()
	T = gauss(f,a,b,2**i)
	end = clock.time()
	error = abs((T-I)/I)
	timeLen = end-start
	mn,sc,ms = watch.stopwatch(timeLen)
	print('{0:3d}\t{1:10.1f}\t{2:10.10f}\t{3:2.10f}\t{4:02}:{5:02}:{6:03}'.format(i,2**i,T,error,mn,sc,ms))
