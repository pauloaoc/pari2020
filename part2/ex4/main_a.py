#!/usr/bin/env python
'''
funcao principal (main)
'''
import readchar


def printAllCharsUpTo(stop_char):
    c = ord(stop_char)
    for i in range(32, c):
        print(chr(i))

def main():
    stop_char = readchar.readchar()
    printAllCharsUpTo(stop_char)


if __name__ == '__main__':
    main()
