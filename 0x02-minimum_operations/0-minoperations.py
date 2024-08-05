#!/usr/bin/python3
"""
Module to calculate minimum operations to achieve n characters in a file
using only Copy All and Paste operations.
"""

def minOperations(n):
    """
    Calculate the minimum number of operations needed to get exactly n H characters.
    
    Parameters:
    n (int): The number of characters to reach
    
    Returns:
    int: Minimum number of operations or 0 if impossible
    """
    if n <= 1:
        return 0

    operations = 0
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            operations += divisor
            n //= divisor
        divisor += 1

    return operations

