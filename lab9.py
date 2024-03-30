#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 30 13:53:25 2024

@author: stephenson
"""

# Initialize a variable to count the lines containing numbers
numeric_lines_count = 0
#init var, numeric_lines_count to count lines with nums, lines 3 4 and 5
# Open the file named "input1.txt"
with open("input1.txt", "r") as file:
# Open the file named "input1.txt", r means read, r is one of 3 possibilities here
    for line in file:
 #this loop reads each line at input1.txt
        print(line.strip())
#log the actual lines to terminal emulator

        if any(char.isdigit() for char in line.strip()):
# Check if the line contains a numeric value, you'll add one to the count initialized at line 10
            numeric_lines_count += 1
# += is adding to the var alloc'd at the stack at line 10 by count 1


print("There are {} lines containing numbers in this data file.".format(numeric_lines_count))
#logging count of lines containing nums to terminal emulator