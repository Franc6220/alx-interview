#!/usr/bin/python3
'''Module to find Pascal's Triangle integers'''

def pascal_triangle(n):
    """
    Returns a list of lists of integers representing Pascal's triangle of n.
    """
    # Return an empty list if n is less than or equal to 0
    if n <= 0:
        return []

    # Initialize the triangle with the first row
    triangle = [[1]]

    # Generate the triangle row by row
    for i in range(1, n):
        # Start the new row with a leading 1
        row = [1]
        
        # Compute the values in the middle of the row
        for j in range(1, i):
            # The value is the sum of the two values above it in the triangle
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        
        # End the row with a trailing 1
        row.append(1)
        
        # Append the completed row to the triangle
        triangle.append(row)

    return triangle

