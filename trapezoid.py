#!/usr/bin/env python3 

"""
========================================================================
MA305 - Lab 9: Jordan James - 11/19/18 
========================================================================
"""
b = 1
a = 0
N = 100
h = (b-a)/N
i = 1

def f(x):
    funct = 4/(1+x**2)
    return funct

def trapRule(b, a, N, h, i):
    myPi = h*(((1/2)*f(a)) + fXSum(i, N) + ((1/2)*f(b)))
    return myPi



def fXSum(i, N):
    N = N - 1
    summ = 0
    for i in range(N):
        xI = a + i * h
        summ = summ + f(xI)
    return summ


pie = trapRule(b, a, N, h, i)
print(pie)
    
