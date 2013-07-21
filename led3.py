#!/usr/bin/python
import RPi.GPIO as GPIO
import time

GPIO.cleanup()
GPIO.setmode(GPIO.BOARD)

GPIO.setup(12, GPIO.OUT)

GPIO.output(12, False)

time.sleep(3)

GPIO.output(12, True)
GPIO.cleanup()