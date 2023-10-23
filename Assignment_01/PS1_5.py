# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 13:04:25 2023

@author: Tianci
"""
import matplotlib.pyplot as plt

# Use ternary to express '+' '-' and '', get the idea from Nan Xingyu
# First define a function to turn number between ternary and decimal
def ten2three(num):
    three_list = []
    while num != 0:
        num, remainder = divmod(num, 3)
        three_list.insert(0, remainder)
    while len(three_list) < 8:
        three_list.insert(0, 0)
    return three_list

# Creat a list to express all the ternary from 00000000 to 22222222
ternary_list = []
for i in range (0,6561):
    ternary_list.append(ten2three(i))

def Find_expression(num):
    # Creat a new dictnory to store all the poslble solution
    all_num = {}
    for i in range(0,len(ternary_list)):
        con_list = ['1']
        # '0' indicate '+', '1' indicate '-'
        for j in range(2,10):
            if ternary_list[i][j-2] == 0:
                con_list.append(str(j))
            elif ternary_list[i][j-2] == 1:
                con_list.append('-'+str(j))
            else:
                con_list[-1] = con_list[-1] + str(j)
        sum = 0
        equ_str = ''
        for k in range(0,len(con_list)):
            sum = sum + int(con_list[k])
            if int(con_list[k]) > 0:
                equ_str = equ_str + '+' + str(con_list[k])
            else:
                equ_str = equ_str + str(con_list[k])
        all_num[equ_str[1:]+'='+str(sum)] = sum
    for key in all_num.keys():
        if all_num[key] == num:
            print(key)
Find_expression(45)

all_num = {}
for i in range(0,len(ternary_list)):
    con_list = ['1']
    # '0' indicate '+', '1' indicate '-'
    for j in range(2,10):
        if ternary_list[i][j-2] == 0:
            con_list.append(str(j))
        elif ternary_list[i][j-2] == 1:
            con_list.append('-'+str(j))
        else:
            con_list[-1] = con_list[-1] + str(j)
    sum = 0
    equ_str = ''
    for k in range(0,len(con_list)):
        sum = sum + int(con_list[k])
        if int(con_list[k]) > 0:
            equ_str = equ_str + '+' + str(con_list[k])
        else:
            equ_str = equ_str + str(con_list[k])
    all_num[equ_str[1:]+'='+str(sum)] = sum
# 
Total_solutions = []        
for i in range(0,100):
    count = 0
    for key in all_num.keys():
        if all_num[key] == i:
            count = count + 1
    Total_solutions.append(count)
x_xls = range(1,101)
max_y = max(Total_solutions)
min_y = min(Total_solutions)
plt.plot(x_xls, Total_solutions)
# 在图上添加文本标签
plt.title("Total solution")
plt.ylabel("Number of solutions")
plt.show()
print(Total_solutions.index(max_y))
print(Total_solutions.index(min_y))
