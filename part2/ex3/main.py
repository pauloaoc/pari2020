#!/usr/bin/env python
'''
funcao principal (main)
'''
import argparse

from my_functions import isPerfect


def main():
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('-nm', '--max_number', type=int, default=100,
                        help='Maximum number to evaluate (default: 100)')
    args = vars(parser.parse_args())
    maximum_number = args['max_number']
    print("Starting to compute perfect numbers up to " + str(maximum_number))

    for i in range(1, maximum_number):  # cicles through every value
        if isPerfect(i):  # tests every value
            print('Number ' + str(i) + ' is perfect.')  # prints if its perfect


if __name__ == "__main__":
    main()
