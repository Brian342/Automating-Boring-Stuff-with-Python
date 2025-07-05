import os

path = '/Users/briankimanzi/Documents/programming Languages/PythonProgramming/Automating-Boring-Stuff-with-Python/Chapter8 Reading and writing Files'

# print(os.path.getsize(path))  # returns the file in bytes of the file in the path argument

print(os.listdir(path))  # returns a list of filename strings for each file in the path argument

# Getting all the total size of all the files in this directory
totalsize = 0
for filename in os.listdir('/Users/briankimanzi'):
    totalsize = totalsize + os.path.getsize(os.path.join())
