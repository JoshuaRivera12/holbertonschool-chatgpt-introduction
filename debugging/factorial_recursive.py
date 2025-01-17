#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calculate the factorial of a non-negative integer using recursion.

    Function Description:
    This function computes the factorial of a given non-negative integer `n` using a recursive approach. 
    The factorial of 0 is defined as 1, and for any positive integer `n`, 
    factorial(n) = n * factorial(n-1).

    Parameters:
    n (int): A non-negative integer whose factorial is to be calculated.

    Returns:
    int: The factorial of the input integer `n`. If `n` is 0, the function returns 1.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Get the integer input from the command line argument
f = factorial(int(sys.argv[1]))

# Print the factorial result
print(f)

