#!/usr/bin/env python
'''
funcao principal (main)
'''
import readchar


def isnumeric(asc):
    if 48 <= asc <= 57:
        return True
    else:
        return False


def countNumbersUpTo(stop_char):
    stop=ord(stop_char)
    inputs = []
    while True:
        a = ord(readchar.readchar())
        if not a == stop:
            inputs.append(a)
        else:
            break

    total_numbers = 0
    total_others = 0

    for input in inputs:
        if isnumeric(input):
            total_numbers += 1
        else:
            total_others += 1

    print('You entered ' + str(total_numbers) + ' numbers.')
    print('You entered ' + str(total_others) + ' others.')


def main():
    countNumbersUpTo('X')


if __name__ == '__main__':
    main()
