#!/usr/bin/python3  # Shebang line to specify the Python 3 interpreter
import sys  # Import the sys module to access command-line arguments

def factorial(n):
    """
    Calculates the factorial of a given number.

    Parameters:
    n (int): The number to calculate the factorial for.

    Returns:
    int: The factorial of n.
    """
    if n == 0:  # Base case: the factorial of 0 is 1
        return 1
    else:
        return n * factorial(n-1)  # Recursive case: the factorial of n is n * factorial(n-1)

# Get the first command-line argument (the number to calculate the factorial for)
f = factorial(int(sys.argv[1]))
print(f)  # Print the calculated factorial