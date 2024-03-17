# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 14:48:32 2024

@author: Gouvernail
"""

class Person:
    def __init__(self, name, age, hobby):
        self.name = name
        self.age = age
        self.hobby = hobby
    
    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old and my hobby is {self.hobby}"

# Creating instances of the Person class
person1 = Person("Alice", 30, "being a thot")
person2 = Person("Bob", 25, "golfing")
person3 = Person("Matthieu", 5000, "parkour")

# Accessing attributes and calling methods
print(person3.name)  # Output: Bob
print(person3.age)   # Output: 25
print(person3.greet())  # Output: Hello, my name is Bob and I am 30 years old.

#so basically, you're crafting your own methods.....in classes. right?
