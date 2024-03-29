"""
Write a Python program that finds and prints the Greatest Common Divisor (GCD)
of the numbers a and b (the largest number that divides them both).
"""
import math


def find_gcd(a, b):
    if b == 0:
        return a
    else:
        return find_gcd(b, a % b)

# import math
# a = 4
# b = 2
#
# math.gcd(4, 2)