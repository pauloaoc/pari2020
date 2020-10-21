#!/usr/bin/env python
'''
funcao principal (main)
'''
import readchar


def separator(list):
    string = ' '.join(list)
    strings = str(string)
    numbers = [x for x in strings if x.isdigit()]
    characters = [x for x in strings if x.isalpha()]
    return numbers, characters


def main():
    inputs = []
    while True:
        a = ord(readchar.readchar())
        if not a == 88:
            inputs.append(a)
        else:
            break
    sep = separator(inputs)
    print(sep[0])


if __name__ == '__main__':
    main()
