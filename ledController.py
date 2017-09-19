#!/usr/bin/python3
# -*- coding: utf-8 -*-

import time
import serial

ser = serial.Serial('/dev/ttyS0')


def turn_on():
    ser.setDTR(True)


def turn_off():
    ser.setDTR(False)


def display_morse(encoded):
    words = encoded.split("/")
    for word in words:
        characters = word.split(" ")
        for character in characters:
            for component in character:
                if (component == '.'):
                    turn_on()
                    time.sleep(0.1)
                    turn_off()
                elif (component == '-'):
                    turn_on()
                    time.sleep(0.3)
                    turn_off()
                time.sleep(0.1)
            time.sleep(0.3)
        time.sleep(0.7)



if __name__ == '__main__':
    print("start")
    turn_on()
    time.sleep(1)
    turn_off()
    time.sleep(1)
    print("end")
