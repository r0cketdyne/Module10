#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 15:34:41 2024

@author: stephenson
"""

#hyper simple for loops python

# Define a sequence (in this case, a list)
arr_matey = [1, 2, 3, 4, 5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20] #list is initialized, which isn't really a list
#it is actually an array of INTS. ffs


# Loop over each element in the sequence
for element in arr_matey:
#    arr_matey.reverse()
    rev_steppin = arr_matey[::-2] #: means entire array, : means end at 
    #so, the general syntax for looping over shit is for, array element, 
    #in the array name "stupidly called my list, despite being an arr
    
    # Print each element
#    print("Current element:", element)

# Print after the loop ends
#print("Loop ended.")
#print("reversed array is", arr_matey)

#aiight lets do some reversals and steppin. some shit was commented out here
print(rev_steppin)


