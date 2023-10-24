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
    #sum of the number at location i and i-1 of previous row. So a mulitdimension 
    # list is need to store all the rows in the pascal triangle. Calcuate the new
    # from from the previous row and append it in the list. do the cycle to get
    # all the triangle until the wanted row
    while len(triangle) < row_num:
        # new row start with 1
        new_row = [1]
        for i in range(1, len(triangle[-1])):
            new_row.append(triangle[-1][i - 1] + triangle[-1][i])
        # new row ended with 1
        new_row.append(1)
        triangle.append(new_row)
    print(triangle[row_num-1])

Pascal_triangle(10)
#Pascal_triangle(200)
