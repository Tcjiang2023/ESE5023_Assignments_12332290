# -*- coding: utf-8 -*-
"""
Created on Sat Oct  7 19:49:02 2023

@author: Jiang
"""

import random
import numpy as np

# 2.1 creat two matrices and fill them with randoms
M1 = np.random.randint(0,50,size=(5,10))
M2 = np.random.randint(0,50,size=(10,5))

# Print to check the matrices
print(M1)
print(M2)

# Define a function to do Matrix multiplication
def Matrix_multip(m1,m2):
    m3 = np.full((5,5),0)
    for i in range(0,5):
        for j in range(0,5):
            for k in range(0,10):
                m3[i,j] = m3[i,j] + m1[i,k]*m2[k,j]
    print(m3)

# Use the function to calculate Matrix multiplication
Matrix_multip(M1, M2)

# Use np.dot() to test to result
print(np.dot(M1,M2))