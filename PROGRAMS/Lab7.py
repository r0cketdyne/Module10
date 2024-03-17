# -*- coding: utf-8 -*-


"""
str4 = "What is your name?"
print(len(str4.split()))
#length will be 4, bc there are 4 items at the list. haven't run it yet
#aaaand I was right.
"""

"""
str4 = "What is your name"
print(str4[2:8:1]) #START AT 2 which is h, stop at 8, step is 1. which means you step back that many from the end of whatever end is for some reason
#what is. is it also logging a single white space bc :1?
#trying 1:3:1
#ha
#these are SLICING RULES.slice step cannot be zero
#[start:stop:step] where the start, stop and step are string indices.
#first str char is 0 , next is 1 and so on

#SYNTAX
#arr[start:stop]         # items start through stop-1
#arr[start:]             # items start through the rest of the array
#arr[:stop]              # items from the beginning through stop-1
#arr[:]                  # a copy of the whole array
#arr[start:stop:step]    # start through not past stop, by step

#here is a y 
#at is y because STOP IS STOP -1. but we knew this.
"""

"""
str1 = "jonah smith"
str3 = str1[::3] #are we slicing the str and only printing a certain part?
str_upp = str3.upper() #used an uppercase method just for funsies
print(str_upp)
#I am actually commenting out the print function and analyzing
#only what appears in sys memory at the stack
#using pythons analysis tool. refresh it always between code snippet tests
#to clear the stack
#so, it appears as though ::4 means to print out only 
#every nth letter at the string. so ::3 would be the first letter and every 3rd
#letter after that. if it was 5, it would print every 5th letter and so on
#so... "::" constrained at [] linked to any given var (string is held there rn)
#means to print every nth num. whatever that num is. if it was 8 you'd print
#every 8th thing at the string. INCLUDING the first value at the string. 
#which in this case is j. I see the trend. just can't convert it
#to english yet
#so in this case jast


"""

"""
str1 = "jonah smith"
str2 = "Jonah smith"

print(str1)
print(str2)

"""

"""
str1 = "jonah smith"
myNames = str1.split()

print(myNames)
#lists are better for sorting data. arrs and lists are two very different data structs 
"""
"""
str1 = "jonah smith"
myNames = str1.split() #will split into ['jonah' , 'smith'] list
newName = "" #assigned but has no val yet
for n in myNames : #for every list value in the list myNames, which holds two values rn

    newName = newName + n.capitalize() + " " # capitalize each list val. so to ['Jonah', 'Smith']
    
print(newName) # it will print out "Jonah Smith"
#moral of story is, to transform data, we need to convert strings to lists and use methods at list elements
"""



