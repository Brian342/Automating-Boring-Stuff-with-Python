import os.path

# print(os.path.abspath('.'))  # returns a string of the absolute path of the argument an easy way to convert
# a relative path into an absolute path

# print(os.path.isabs('/user'))  # returns true if the argument is an absolute path and False if it's a relative path

# print(os.path.relpath('/Users', '/PythonProgramming/Automating-Boring-Stuff-with-Python'))
# returns a string of a relative path from start path to path

# print(os.getcwd())

# path = '/Users/briankimanzi/Documents/programming Languages/PythonProgramming/Automating-Boring-Stuff-with-Python/Chapter8 Reading and writing Files'
# print(os.path.basename(path))  # returns a string of everything that comes after the last slash in the path argument

# print(os.path.dirname(path))  # returns a string of everything that comes before the last slash in the path argument

calcFilePath = '/Users/briankimanzi/Documents/programming Languages/PythonProgramming/Automating-Boring-Stuff-with-Python/Chapter8 Reading and writing Files'
# print(os.path.split(calcFilePath)) # returns the base name and dir path together
# print((os.path.dirname(calcFilePath), os.path.basename(calcFilePath)))  # returns the base name and dir path together

print(calcFilePath.split(os.path.sep))
