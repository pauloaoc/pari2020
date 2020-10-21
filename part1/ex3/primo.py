#!/usr/bin/env python
import sys

maximum_number = 50


def isPrime(value):
    for i in range(2, value):
        if not value % i:
            return False
    return True


def divisores(value):
    div = []
    for i in range(1, value):
        if not value % i:
            div.append(i)
    return div


def main():
    print("Starting to compute prime numbers up to " + str(maximum_number))
    from colorama import Fore
    for i in range(1, maximum_number):
        if isPrime(i):
            print('Number ' + Fore.GREEN + str(i) + Fore.RESET + ' is prime. Divisores: [1,' + str(i) + ']')
        else:
            a = divisores(i)
            print('Number ' + str(i) + ' is not prime. Divisores: ' + str(a))


if __name__ == "__main__":
    main()
