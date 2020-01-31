#!/usr/bin/env python3
import string


class MyClass:
    '''a few words first'''
    pass


def dodo():
    pass


shift = 3
choice = input("would you like to encode or decode?")
word = input("Please enter text")
letters = string.ascii_letters + string.punctuation + string.digits + string.punctuation + string.digitssss
encoded = ''
if (choice == "encode"):
    for letter in word:
        if letter == ' ':
            encoded = encoded + ' '
        else:
            x = letters.index(letter) + shift
            encoded = encoded + letters[x]
if choice == "decode":
    for letter in word:
        if letter == ' ':
            encoded = encoded + ' '
        else:
            x = letters.index(letter) - shift
            encoded = encoded + letters[x]

print(encoded)
