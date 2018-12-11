#!usr/bin/env python3
"""
=====

=====
"""

def stopwatch(time):

	valueD = (((time/365)/24)/60)
	days = int(valueD)
	
	valueH = (valueD-days)*365
	hours = int(valueH)
	
	valueM = (valueH-hours)*24
	minutes = int(valueM)
	
	valueS = (valueM-minutes)*60
	seconds = int(valueS)


	valueMS = (valueS-seconds)*1000
	milli = int(valueMS)

	return minutes,seconds,milli
	
