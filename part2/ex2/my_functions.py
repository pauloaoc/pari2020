#!/usr/bin/env python
'''
funcao teste de numeros
'''
def isPerfect(value):
    sum=0
    for i in range(1, value):
        if not value % i:     #finds every divider
            sum += i      #sums every divider
    if sum == value:      #compairs the sum to the original value
        return True
    else:
        return False
