#!/usr/bin/env python

maximum_number = 100

def isPerfect(value):
    sum=0
    for i in range (1,value):
        if not value%i:
            sum+=i
    if sum==value:
        return True
    else:
        return False

def main():
    print("Starting to compute perfect numbers up to " + str(maximum_number))

    for i in range(1, maximum_number):
        if isPerfect(i):
            print('Number ' + str(i) + ' is perfect.')


if __name__ == "__main__":
    main()
