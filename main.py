#!/usr/bin/python3
# -*- coding: utf-8 -*-

import time
import morseTranslator
import ledController


if __name__ == '__main__':
    '''
        phrase = "The quick brown fox jumps over the lazy dog 1234567890"
        print(phrase)
        encoded = morseTranslator.encode(phrase)
        print(encoded)
        decoded = morseTranslator.decode(encoded)
        print(decoded)
        ledController.display_morse(morseTranslator.encode(encoded))
    '''
    while (True):
        a = input()
        if (not a):
            break
        ledController.display_morse(morseTranslator.encode(a))

