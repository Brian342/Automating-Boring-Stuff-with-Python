# step1: comments and shelf setup
# mcb.pyw - saves and loads pieces of text to the clipboard
# usage: py.exe mcb.pyw save <keyword> - Saves clipboard to keyword
# py.exe mcb.pyw <keyword> - loads keyword to clipboard
# py.exe mcb.pyw list - Loads all keywords to clipboard

import shelve, pyperclip, sys

mcbShelf = shelve.open('mcb')

mcbShelf.close()

# step2: Save clipboard Content with a keyword
# save clipboard content