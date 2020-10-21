#!/usr/bin/env python
'''
Responds with every perfect value from 0 to 100
'''
maximum_number = 100

def isPerfect(value):
    sum=0
    for i in range (1,value):
        if not value%i:     #finds every divider
            sum+=i      #sums every divider
    if sum==value:      #compairs the sum to the original value
        return True
    else:
        return False

def main():
    print("Starting to compute perfect numbers up to " + str(maximum_number))

    for i in range(1, maximum_number):      #cicles through every value
        if isPerfect(i):        #tests every value
            print('Number ' + str(i) + ' is perfect.')      #prints if its perfect


if __name__ == "__main__":
    main()
