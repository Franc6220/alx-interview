def pascal_triangle(n):
    """
    Returns a list of lists of integers representing Pascal's triangle of n.
    """
    if n <= 0:
        return []

    triangle = [[1]]  # Initialize the triangle with the first row

    for i in range(1, n):
        row = [1]  # The first element of each row is always 1
        for j in range(1, i):
            # Calculate the value of the current element
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)  # The last element of each row is always 1
        triangle.append(row)

    return triangle

