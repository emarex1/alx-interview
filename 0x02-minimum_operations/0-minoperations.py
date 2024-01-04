#!/usr/bin/python3
""" Module for 0-minoperations"""


def minOperations(n):
    """
    minOperations
    Gets fewest # of operations needed to result in exactly n H characters
    """
    if n == 1:
        return 0
    
    # Initialize variables
    result = n  # At most, n operations are needed
    divisor = 2  # Start dividing by 2
    
    while divisor <= n:
        if n % divisor == 0:
            # If n is divisible by the divisor, check the operations needed for divisor copies
            result = min(result, minOperations(n // divisor) + divisor)
        
        divisor += 1
    
    return result
