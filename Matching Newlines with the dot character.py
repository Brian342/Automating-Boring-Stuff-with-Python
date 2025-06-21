import re

noNewLineRegex = re.compile('.*')
# print(noNewLineRegex.search('Serve the public trust.\nprotect the innocent.\nUphold the law').group())

NewLineRegex = re.compile('.*', re.DOTALL)
print(NewLineRegex.search('Serve the public trust.\nprotect the innocent.\nUphold the law').group())
