#!/usr/bin/env python3 

"""
========================================================================
MA305 - Lab 9: Jordan James - 11/19/18 
========================================================================
"""
import random
throws = 1000000

def dartBoard(throws):
    dartsInCircle = 0
    
    for i in range(throws):
        x = random.random()/1.0
        y = random.random()/1.0
        if(1 > (x * x) + (y * y)):
            dartsInCircle = dartsInCircle + 1


    myPi = 4 * dartsInCircle/throws
    print(myPi)

dartBoard(throws)
