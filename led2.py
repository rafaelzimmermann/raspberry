#!/usr/bin/python
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)

GPIO_BUTTON_INPUT = 11
GPIO_BUTTON_OUTPUT = 12

while True:
	if GPIO.input(GPIO_BUTTON_INPUT):
		GPIO.output(12, True)
		print "GPIO 12",True
	else:
		GPIO.output(12, False)
		print "GPIO 12",False