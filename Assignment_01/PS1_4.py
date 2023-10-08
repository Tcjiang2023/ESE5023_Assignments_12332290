# -*- coding: utf-8 -*-
"""
Created on Sun Oct  8 09:23:07 2023

@author: Jiang
"""
# Define the function Least_moves() to calculate how many steps are needed to 
# reach 'x' by performing calculations starting from 'x'. If 'x' is odd,
# subtract 1 to obtain a new 'x'; if 'x' is even, divide it by 2 to get a new
# 'x', and repeat the process until 'x' equals 1.

def Least_moves(x):
    move = 0
    while x != 1:
        if x%2 != 0:
            x = x-1
            move = move +1
        if x%2 == 0:
            x = x / 2
            move = move + 1
    print(move)

# test the function
Least_moves(7)