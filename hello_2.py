#!/usr/bin/env python3
import os
a = 1

os.system('clear')


def ex_1():
    if (a == 1):
        print('Hello World!')
    else:
        print('Ciao, Ciao, Ciao, Ciao, Ciao, Ciao, Ciao, Ciao, Ciao, Ciao, Ciao, Ciao, Ciao, Ciao, Ciao, Ciao, Ciao, C')

    def ex_2():
        b = 2
        print(f'b = {b}')

    ex_2()
    print('after ex_2')


def ex_3():
    for i in range(8):
        print(f'Je te l\'ai dit {i} fois')
        msg = 'world'
        print(i*f'Hello {msg} ')


def main():
    ex_3()


if __name__ == '__main__':
    main()
