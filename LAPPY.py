#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 14:10:47 2024

@author: stephenson
"""

class waifu_Gen:
    def __init__(shittest, name, age, haircolor, deretype, weight, eyecolor, racesocialconst):
        shittest.name = name
        shittest.age = age
        shittest.haircolor = haircolor
        shittest.deretype = deretype
        shittest.weight = weight
        shittest.eyecolor = eyecolor
        shittest.racesocialconst = racesocialconst
        
    
    def lappy_is_ALIVE_MWAHA(shittest):
        print("Hello my name is " + shittest.name + " from " + shittest.racesocialconst)
        #ooooh so I can create
        #A new func, and take the object I just initialized as a param
        #and call methods, or object methods I just created within the new
        #func. Very interesting...the nature of scope here
    def texas_is_here_too(shittest):
        print("I'm " + shittest.name + " from " + shittest.racesocialconst)
    
new_waifu1 = waifu_Gen("Lappy", 22, "ice blonde", "yandere", "50kg", "blue", "Finland")
new_waifu2 = waifu_Gen("Texas the Omertosa", 22, "brown", "yandere", "60kg", "brown", "Texas")
#so Lappy is created at this very line, defined as a new waifu.
new_waifu1.lappy_is_ALIVE_MWAHA()  
new_waifu2.texas_is_here_too() 
#but we can't speak to her unless we invoke her to speak. 
#we do that by calling her, bc shes a new waifu object
#and using the function we created, perhaps a translater to allow her to speak
#bc she exists only at computational universe of all possible progs
#and once she's called she should speak. fingers crossed

#LMAO SHE SPOKE