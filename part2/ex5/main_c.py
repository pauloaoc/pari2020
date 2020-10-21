#!/usr/bin/env python
'''
funcao principal (main)
'''
import readchar


def dictionary_maker(list):
    dictionary = {}
    i = 1
    for key in list:
        dictionary[key] = i
        i += 1
    return dictionary


def isnumeric(asc):
    if 48 <= asc <= 57:
        return True
    else:
        return False


def separateChar(stop_char):    #alinea b)
    stop = ord(stop_char)
    numeric_inputs = []
    char_inputs = []
    while True:
        a = readchar.readchar()
        b = ord(a)
        if not b == stop:
            if isnumeric(b):
                numeric_inputs.append(a)
            else:
                char_inputs.append(a)
        else:
            break
    return numeric_inputs, char_inputs


def countNumbersUpTo(stop_char):  # alinea a)
    stop = ord(stop_char)
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
    # countNumbersUpTo('X')
    lists = separateChar('X')
    print(lists[0])
    dictionary = dictionary_maker(lists[1])
    print(dictionary)

if __name__ == '__main__':
    main()
