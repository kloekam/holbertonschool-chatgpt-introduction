#!/usr/bin/python3
import sys  

    # Function Description:
     # This function calculates the factorial of a given non-negative integer using recursion.
     # The factorial of a number n (written as n!) is the product of all positive integers less than or equal to n.
     # Factorial is widely used in mathematical computations such as permutations, combinations, and probability.
    


def factorial(n):
    # Parameter:
    #   n (int): The non-negative integer for which the factorial is to be computed.
    
    # If n is 0, return 1 (base case of factorial)
    if n == 0:
        return 1
    else:
        # Recursive case: multiply n by the factorial of (n-1)
        return n * factorial(n - 1)

# Get the input number from command-line arguments
# sys.argv[1] represents the first argument entered after the script name
f = factorial(int(sys.argv[1]))

# Print the result of the factorial calculation
print(f)