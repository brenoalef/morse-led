#!/usr/bin/python3
# -*- coding: utf-8 -*-

import morseTranslator
import time


def display_morse(morse):
    for c in morse:
        print(c)
        if (c == '.' or c == ' '):
            time.sleep(0.1)
        elif (c == '-'):
            time.sleep(0.3)
        elif (c == '/'):
            time.sleep(0.7)


if __name__ == '__main__':
    phrase = "The quick brown fox jumps over the lazy dog 1234567890"
    print(phrase)
    encoded = morseTranslator.encode(phrase)
    print(encoded)
    decoded = morseTranslator.decode(encoded)
    print(decoded)
    #display_morse(morseTranslator.encode(encoded))

'''
    while (True):
        a = input()
        if (not a):
            break
        display_morse(morseTranslator.encode(a))
'''