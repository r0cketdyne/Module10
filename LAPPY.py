#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 14:10:47 2024

@author: stephenson
"""

class waifu_Gen:
    def __init__(shittest, name, age, haircolor, deretype, weight, eyecolor):
        shittest.name = name
        shittest.age = age
        shittest.haircolor = haircolor
        shittest.deretype = deretype
        shittest.weight = weight
        shittest.eyecolor = eyecolor
        
    
new_waifu1 = waifu_Gen("Lappy", 22, "ice blonde", "yandere", "50kg", "blue")

print(new_waifu1.name, new_waifu1.haircolor)
