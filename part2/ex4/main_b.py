#!/usr/bin/env python
'''
funcao principal (main)
'''
import readchar


def readAllUpTo(stop_char):
    c = ord(stop_char)
    while c<120:
        print(stop_char)

def main():
    stop_char = readchar.readchar()
    readAllUpTo(stop_char)


if __name__ == '__main__':
    main()
