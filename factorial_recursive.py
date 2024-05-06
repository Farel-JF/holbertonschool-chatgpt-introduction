#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calculate the factorial of a given number using recursion.

    Function Description:
    ----------------------
    This function calculates the factorial of a non-negative integer using recursion.
    The factorial of a non-negative integer n, denoted as n!, is the product of all positive integers less than or equal to n.

    Parameters:
    -----------
    n : int
        The non-negative integer for which the factorial is to be calculated.

    Returns:
    --------
    int
        The factorial of the input integer n.
    """
    if n == 0:  # Base case: If n is 0, return 1
        return 1
    else:
        # Recursive case: Multiply n with the factorial of (n-1)
        return n * factorial(n-1)

# Get the input integer from the command line argument
input_integer = int(sys.argv[1])

# Calculate the factorial of the input integer using the factorial function
result = factorial(input_integer)

# Print the factorial of the input integer
print(result)
