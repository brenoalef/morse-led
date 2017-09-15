#!/usr/bin/python3
# -*- coding: utf-8 -*-

alphabet_to_morse = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "Ä": ".-.-",
    "À": ".--.-",
    "Á": ".--.-",
    "Å": ".--.-",
    "Ch": "----",
    "É": "..-..",
    "È": ".-..-",
    "Ñ": "--.--",
    "Ö": "---.",
    "Ü": "..--",
    ".": ".-.-.-",
    ",": "--..--",
    ":": "---...",
    ";": "-.-.-.",
    "?": "..--..",
    "-": "-....-",
    "_": "..--.-",
    "(": "-.--.",
    ")": "-.--.-",
    "'": ".----.",
    "=": "-...-",
    "+": ".-.-.",
    "/": "-..-.",
    "@": ".--.-.",
    " ": "/",
    "" : ""
}

morse_to_alphabet = {
    v: k for k, v in alphabet_to_morse.items()
}


def filter_characters(string):
    return ''.join(filter(lambda char: char in alphabet_to_morse, string.upper()))


def encode(decoded):
    encoded = []

    words = filter_characters(decoded).upper().split(" ")
    for word in words:
        morseword = []

        for character in word:
            morseword.append(alphabet_to_morse[character])

        encoded.append(" ".join(morseword))

    return "/".join(encoded)


def decode(encoded):
    decoded = []

    words = encoded.split("/")
    for word in words:
        decodedword = []
        characters = word.split(" ")

        for character in characters:
            decodedword.append(morse_to_alphabet[character])

        decoded.append("".join(decodedword))

    return " ".join(decoded)