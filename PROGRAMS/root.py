# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 10:15:32 2024

@author: Gouvernail
"""

# example_8-2.py
# Version 2, modified with counter and "close enough" tolerance for the guess!
#
# use the newtonian method to estimate the square root of a number
# Algorithm Steps
# After prompting the user for a number,
# make an initial guess. Use the original number as the first guess.
# As long as the difference between the guesses are larger than the tolerance
# Divide the original number by the old guess
# Take this result and average it with the old guess to create a new guess
# check the difference to determine whether to
#
# Variables used in this program:
# N the number to compute the square root for
# count keep track of how many guesses it took to get to the result
# old_guess the guessed square root value from the prior attempt
# new_guess the guessed square root value for the current attempt
# quotient the result of dividing N by a guess
# tolerance when the difference between two guesses is less than this
# amount, then we are within range
#
###############################################################################
count = 1
N = float(input("Enter a number to compute square root for: "))
tolerance = 0.000001
old_guess = N # make first guess
new_guess = N/2
while abs(new_guess - old_guess) > tolerance :
    old_guess = new_guess
quotient = N/old_guess
new_guess = (old_guess + quotient)/2
count = count + 1
print("After {:>3d} guesses, the square root is {:.4f}".format(count, new_guess))

