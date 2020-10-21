#!/usr/bin/env python
'''
funcao principal (main)
'''
import readchar


def isnumeric(char):
    asc = ord(char)
    if 48 <= asc <= 57:
        return True
    else:
        return False


def main():
    total_numbers = 0
    total_others = 0
    while True:
        i = readchar.readchar()
        if i == "X":
            break
        if isnumeric(i):
            total_numbers += 1
        else:
            total_others += 1

    print('You entered ' + str(total_numbers) + ' numbers.')
    print('You entered ' + str(total_others) + ' others.')


if __name__ == '__main__':
    main()
