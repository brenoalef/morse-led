#!/usr/bin/python3
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(18, GPIO.OUT)


def turn_on():
    print("LED ON\n")
    GPIO.output(18, 1)


def turn_off():
    print("LED OFF")
    GPIO.output(18, 0)


def display_morse(encoded):
    for c in encoded:
        print(c)
        if (c == '.' or c == ' '):
            time.sleep(0.1)
        elif (c == '-'):
            time.sleep(0.3)
        elif (c == '/'):
            time.sleep(0.7)


if __name__ == '__main__':
    print("start")
    turn_on()
    time.sleep(1)
    turn_off()
    time.sleep(1)
    print("end")
