import os.path

# print(os.path.abspath('.'))  # returns a string of the absolute path of the argument an easy way to convert
# a relative path into an absolute path

# print(os.path.isabs('/user'))  # returns true if the argument is an absolute path and False if it's a relative path

print(os.path.relpath('/Users', '/PythonProgramming/Automating-Boring-Stuff-with-Python'))  # returns a string of a relative path from start path to path

print(os.getcwd())