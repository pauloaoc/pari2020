#!/usr/bin/env python
import math
from time import time, ctime


def main():
    t0 = time()
    a = []
    for i in range (0,50000000):
        a.append(math.sqrt(i))
    t1 = time() - t0
    t2 = ctime()
    print("this is Ex1 and the current date is " + t2 +
          "Ellapsed time: " + str(t1) + "seconds")


if __name__ == "__main__":
    main()
