import re

beginsWithHello = re.compile(r'^Hello')
# print(beginsWithHello.search('Hello World'))
# print(beginsWithHello.search('He said Hello.') is None)

# The r'\d$