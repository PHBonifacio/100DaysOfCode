#!/bin/python3

#Given an integer, , perform the following conditional actions:

# If n is odd, print Weird
# If n is even and in the inclusive range 2 of 5  to , print Not Weird
# If n is even and in the inclusive range 6 of 20 to , print Weird
# If n is even and greater than , print Not Weird
import math
import os
import random
import re
import sys

if __name__ == '__main__':
    N = int(input())
    if( ( N % 2 ) == 1 or ( 5 < N and N < 21) ):
        print("Weird")
    else:
        print("Not Weird")