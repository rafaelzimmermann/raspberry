#!/usr/bin/python
import sys
import time
import RPi.GPIO as GPIO


ROTATION_SEQUENCE = [
    [True, False, False, True],
    [True, False, False, False],
    [True, True, False, False],
    [False, True, False, False],
    [False, True, True, False],
    [False, False, True, False],
    [False, False, True, True],
    [False, False, False, True]
]

class StepMotor:

    def __init__(self, gpio_out0, gpio_out1, gpio_out2, gpio_out3):
        GPIO.setmode(GPIO.BCM)
        self.set_pins = [gpio_out0, gpio_out1, gpio_out2, gpio_out3]
        self.position = 0
        self.reset()


    def move_left(self, step_interval_sec, steps):
        for rotation_index in range(0, steps):
            self.position = (self.position + 1) % len(ROTATION_SEQUENCE)
            for pin in range(0, len(self.set_pins)):
              GPIO.output(self.set_pins[pin], ROTATION_SEQUENCE[self.position][pin])
            time.sleep(step_interval_sec)

    def move_right(self, step_interval_sec, steps):
        for rotation_index in range(0, steps):
            self.position = (self.position - 1)
            if self.position < 0:
                self.position = len(ROTATION_SEQUENCE) - 1
            for pin in range(0, len(self.set_pins)):
              GPIO.output(self.set_pins[pin], ROTATION_SEQUENCE[self.position][pin])
            time.sleep(step_interval_sec)

    def reset(self):
        for pin in self.set_pins:
          GPIO.setup(pin, GPIO.OUT)
          GPIO.setwarnings(False)
          GPIO.output(pin, False)

if __name__ == '__main__':
    move_motor = StepMotor(06,13,19,26)
    move_motor.move_left(0.001, 4200)
    move_motor.move_right(0.001, 4200)
    move_motor.reset()
