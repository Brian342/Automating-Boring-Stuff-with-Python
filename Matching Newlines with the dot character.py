import re

noNewLineRegex = re.compile('.*')
print(noNewLineRegex.search('Serve the public trust.\nprotect the innocent.\nUphold the law').group())