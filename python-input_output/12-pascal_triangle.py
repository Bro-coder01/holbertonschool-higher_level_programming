#!/usr/bin/python3
"""
This module provides a function to generate Pascal's Triangle.
"""


def pascal_triangle(n):
    """Returns a list of lists of integers representing Pascal's triangle of n.

    Returns an empty list if n <= 0.
    """
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        prev_row = triangle[-1]
        # كل سطر يبدأ بـ 1
        current_row = [1]

        # حساب العناصر الداخلية بناءً على السطر السابق
        for j in range(1, i):
            current_row.append(prev_row[j - 1] + prev_row[j])

        # كل سطر ينتهي بـ 1
        current_row.append(1)
        triangle.append(current_row)

    return triangle
