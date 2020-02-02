#!/usr/bin/env python3


def increment(x):
    return x + 1


def decrement(x):
    if (x == x):
        print('ok')
    return x - 1


def call():
    x = 3
    increment(x)
    decrement(x)


def main():
    print(increment(0))
    print(decrement(0))


main()
