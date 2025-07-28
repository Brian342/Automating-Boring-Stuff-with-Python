# Task 3: Word Counter
# Description: Create a Python program that reads a text file and counts the number of words in it.
# Objectives:
# Read the content of a file.
# Split the content into words and count them. Handle exceptions, such as file not found.

import os
# Objective 1
filepath = "/Users/briankimanzi/Documents/programmingLanguages/PythonProgramming/Automating-Boring-Stuff-with-Python/SampleFile"
try:
    with open(filepath, 'r') as file:
        content = file.read()
        Words = content.split()
        WordsLen = len(Words)
        print(f"The words count is {WordsLen}")
except FileNotFoundError as e:
    print('File does not exist!!')
except Exception as e:
    print("An error occured")

