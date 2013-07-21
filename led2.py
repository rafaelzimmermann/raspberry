#!/usr/bin/python
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)

GPIO_BUTTON_INPUT = 11
GPIO_BUTTON_OUTPUT = 12

GPIO.setup(GPIO_BUTTON_INPUT, GPIO.IN)
GPIO.setup(GPIO_BUTTON_OUTPUT, GPIO.OUT)

while True:
	if GPIO.input(GPIO_BUTTON_INPUT):
		GPIO.output(12, True)
		print "GPIO 12",True
	else:
		GPIO.output(12, False)
		print "GPIO 12",False