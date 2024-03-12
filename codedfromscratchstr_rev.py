#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 16:50:01 2024

@author: stephenson
"""

str_back = "Reverse the string"
str_rev = (str_back[::-1])

for index, nextletter in enumerate(str_rev): 
    if nextletter.lower() in 'aeiou' :
        #print only vowels
        #added lowercase method here/ python has a TON of string method and manipulation stuff
        print(index, nextletter)
#lmao I actually coded this from scratch. seems to work

#CAN ENUMERATE BE USED TO PRINT KEY VALUE PAIRS????? YEEEET


#FIND USEFUL FEATURES FOR STRING WORK IN PYTHON. TO DO

#MASTER STRING FUNCTIONS. THIS IS THE WAY