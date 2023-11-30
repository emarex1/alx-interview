#!/usr/bin/env python3
"""Pascal Triangle Interview Challenge"""


"""def pascal_triangle(n):
    returns a list of lists of numbers
    representing the pascal triangle
    if n <= 0:
        return []

    pascal_triangle = [0] * n

    for i in range(n):
        # define a row and fill first and last idx with 1
        new_row = [0] * (i+1)
        new_row[0] = 1
        new_row[len(new_row) - 1] = 1

        for j in range(1, i):
            if j > 0 and j < len(new_row):
                a = pascal_triangle[i - 1][j]
                b = pascal_triangle[i - 1][j - 1]
                new_row[j] = a + b

        pascal_triangle[i] = new_row

    return pascal_triangle

def pascal_triangle(n):
    if n <= 0:
        return []

    triangle = []
    for i in range(n):
        row = [1] * (i + 1)
        for j in range(1, i):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        triangle.append(row)

    return triangle"""


def pascal_triangle(n):
    if n <= 0:
        return []
    result = []
    for line in range(1, n + 1):
        C = 1
        row = []
        for i in range(1, line + 1):
            row.append(C)
            C = int(C * (line - i) / i)
        result.append(row)
    return result
