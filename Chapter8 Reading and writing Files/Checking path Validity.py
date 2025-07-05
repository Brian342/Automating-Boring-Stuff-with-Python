import os

path = '/Users/briankimanzi/Documents/programming Languages/PythonProgramming/Automating-Boring-Stuff-with-Python/Chapter8 Reading and writing Files'
path2 = '/Users/briankimanzi/Documents/programming Languages/PythonProgramming/Automating-Boring-Stuff-with-Python/Chapter8 Reading and writing Files/Checking path Validity.py'
# print(os.path.exists(path))
# The above code will return True if the file or folder referred to in the argument exists and False if it doesn't

# print(os.path.isfile(path2))  # returns true if the path argument exists and is a file and will return False otherwise

# print(os.path.isdir(path))  # return True if the path argument exists and is a folder and will return False otherwise

print(os.path.exists('Rickest'))  # checks if a flash drive is attached in your computer
