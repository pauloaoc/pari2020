#!/usr/bin/env python


def addcomplex(x,y):
    xr = x[0]
    xi = x[1]
    yr = y[0]
    yi = y[1]
    soma_r = xr + yr
    soma_i = xi + yi
    soma = (soma_r , soma_i)
    return soma

def multiplycomplex(x,y):
    xr = x[0]
    xi = x[1]
    yr = y[0]
    yi = y[1]
    mult_r = xr * yi - (yr * xi)
    mult_i = xr * yi + xi * yr
    mult = (mult_r, mult_i)
    return mult

def printcomplex(x):
    print(str(x[0]) + ", " + str(x[1]) + "i")



def main():
    c1 = (5, 3)
    c2 = (-2, 7)

    # Test add
    c3 = addcomplex(c1, c2)
    printcomplex(c3)

    # test multiply
    printcomplex(multiplycomplex(c1, c2))


if __name__ == "__main__":
    main()
