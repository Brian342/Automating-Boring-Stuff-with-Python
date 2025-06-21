import re

beginsWithHello = re.compile(r'^Hello')
print(beginsWithHello.search('Hello World'))

