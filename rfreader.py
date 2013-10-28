import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.IN)
while True:
	rfInput = GPIO.input(11)
	if rfInput == False:
		print 1
	else:
		print 0