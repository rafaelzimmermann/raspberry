#!/usr/bin/python
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)
count = 0
while True:
	GPIO.output(11, True)

	count = count + 1
	print "Yahoo!", count
	time.sleep(.2)
	GPIO.output(11, False)
	time.sleep(.2)