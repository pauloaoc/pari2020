#!/usr/bin/env python
'''
funcao principal (main)
'''
from my_functions import isPerfect
maximum_number = 100
def main():
    print("Starting to compute perfect numbers up to " + str(maximum_number))

    for i in range(1, maximum_number):      #cicles through every value
        if isPerfect(i):        #tests every value
            print('Number ' + str(i) + ' is perfect.')      #prints if its perfect


if __name__ == "__main__":
    main()
