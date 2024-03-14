#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 13:43:55 2024

@author: stephenson
"""

#we are gonna create a class that generated humans

class HumanGen:
    def __init__(self, namaewa, age, hobby):
        self.namaewa = namaewa
        self.age = age
        self.hobby = hobby
    def __str__(self):
        return f"{self.namae}{self.age}"
        


newdude1 = HumanGen("Matthew", 4669, "Parkour")
newdude2 = HumanGen("Dinosaur", 22, "Eating")
newdude3 = HumanGen("Dorsal_Fin", 21, "Being Sus")

print(newdude1.namaewa, newdude2.age, newdude3.namaewa)