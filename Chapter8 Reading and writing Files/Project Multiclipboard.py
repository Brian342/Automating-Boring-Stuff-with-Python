# step1: comments and shelf setup
# mcb.pyw - saves and loads pieces of text to the clipboard
#
import shelve, pyperclip, sys

mcbShelf = shelve.open('mcb')

mcbShelf.close()
