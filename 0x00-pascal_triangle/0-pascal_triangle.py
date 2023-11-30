#!/usr/bin/python3
"""Pascal Triangle Interview Challenge"""


def pascal_triangle(n):
    """outer loop"""
    if n <= 0:
        return []
    result = []
    for line in range(1, n + 1):
        """inner loop"""
        C = 1
        row = []
        for i in range(1, line + 1):
            row.append(C)
            C = int(C * (line - i) / i)
        result.append(row)
    return result
