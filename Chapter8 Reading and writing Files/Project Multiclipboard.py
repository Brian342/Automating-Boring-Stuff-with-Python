# step1: comments and shelf setup
# mcb.pyw - saves and loads pieces of text to the clipboard
# usage: py.exe mcb.pyw save <keyword> - Saves clipboard to keyword
#
import shelve, pyperclip, sys

mcbShelf = shelve.open('mcb')

mcbShelf.close()
