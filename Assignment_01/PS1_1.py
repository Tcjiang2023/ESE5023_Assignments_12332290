# -*- coding: utf-8 -*-
"""
Created on Sat Oct  7 19:22:30 2023

@author: Jiang
"""
import random

# Define Print_values with arguments a,b,c, which can print the three input in
#the order from high to low

def Print_values(a,b,c):
    if a>b:
        if b>c:
            print(a,b,c)
        elif a>c:
            print(a,c,b)
        else:
            print(c,a,b)
    elif b>c:
        if a>c:
            print(b,a,c)
        else:
            print(b,c,a)
    else:
        print(c,b,a)

# Creat three random number to test the function
a = random.randint(1,100)
b = random.randint(1,100)
c = random.randint(1,100)

# Use the three random number to test the function
Print_values(a, b, c)
