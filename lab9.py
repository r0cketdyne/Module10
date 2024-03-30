#Lab9 (implementation 1,2,3)
#Matthew Stephenson
#This prog takes a .txt as an input by reading at r, reads each line and 
#logs to standard i/o, closes file and terminates prog.
#added implementation to read each line in order to count 
#the number of lines that contain a numeric val
#logic injected to prompt the user for the input filename at term. emulator
############################################################################
import os  
# Import the os module for file operations
#This mod provides a portable way of using operating system dependent functionality.


filename = input("Please inject the actual filename at pwd: ")
# Prompt the user for the input filename and store it at the stack at filename var

if os.path.exists(filename):
# Check if the file exists within a given directory at pwd
   
    numeric_lines_count = 0
# Initialize var to cnt the lines containing nums

  
    with open(filename, "r") as file:
# Open the actual file. r is one of three possible commands here to read
      
        for line in file:
# Read each line from the file > by > 
         
            print(line.strip())
# log the particular line to screen at standard i/o. strip is just a method

           
            if any(char.isdigit() for char in line.strip()):
# Check if the line contains a num. using isdigit method instead of coding from scratch
                numeric_lines_count += 1  
# Increment the count of numeric lines
# log to standard i/o
    print("There are {} lines containing numbers in this data file.".format(numeric_lines_count))
    # log the count of lines containing numbers to standard i/o
else:
    print("The file '{}' doesnt actually exist. List everything at pwd with ls and try again".format(filename)) 
# if file doesn't exist, log to standard i/o
