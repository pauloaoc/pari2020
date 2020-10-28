#!/usr/bin/env python

#from collections import namedtuple
#Complex = namedtuple('Complex', ['r','i'])

class complex:

    def __init__(self, r, i):
        self.r = r
        self.i = i

    def __str__(self):
        return str(self.r) + ", " + str(self.i) + "i"

    def addcomplex(self,y):
        self.r += y.r
        self.i += y.i

#    def multicomplex(self,y):
#        se

def multiplycomplex(x,y):
    xr = x[0]
    xi = x[1]
    yr = y[0]
    yi = y[1]
    mult_r = xr * yi - (yr * xi)
    mult_i = xr * yi + xi * yr
    mult = complex(mult_r, mult_i)
    return mult

def main():
    c1 = complex(r=5, i=3)
    c2 = complex(-2,7)
    print("Initial c1: " + str(c1))
    print("Initial c2: " + str(c2))
    c1.addcomplex(c2)
    print("c1 + c2 (stored in c1): " + str(c1))

if __name__ == "__main__":
    main()
