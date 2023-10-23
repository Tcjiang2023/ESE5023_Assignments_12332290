# -*- coding: utf-8 -*-
"""
Created on Sat Oct  7 20:33:33 2023

@author: Jiang
"""

# According to the definition of Pascal triangle, the 
def Pascal_triangle(row_num):
    # Define ac to store the 'triangle'
    triangle = [[1]]
    # All the number at location i except the first one and last one are the
    #sum of the number at location i and i-1, so an array prev_row is needed to 
    # calculate the new_row, do the cycle to get all the triangle until the 
    # wanted row
    while len(triangle) < row_num:
        prev_row = triangle[-1]
        # new row start with 1
        new_row = [1]
        for i in range(1, len(prev_row)):
            new_row.append(prev_row[i - 1] + prev_row[i])
        # new row ended with 1
        new_row.append(1)
        triangle.append(new_row)
    print(triangle[row_num-1])

Pascal_triangle(100)
Pascal_triangle(200)
