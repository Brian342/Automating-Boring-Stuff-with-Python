import re

beginsWithHello = re.compile(r'^Hello')
# print(beginsWithHello.search('Hello World'))
# print(beginsWithHello.search('He said Hello.') is None)

# The r'\d$ expression string matches strings that end with a numerical character from 0 to 9
endsWithNumber = re.compile(r'\d$')
# print(endsWithNumber.search('Your number is 42'))
# print(endsWithNumber.search('Your number is forty two') is None)

# The r'\d+$ expression string matches strings that both begin and end with one or more numerical characters
wholeStringIsNum = re.compile(r'^\d+$')
print(wholeStringIsNum.search('1234567890'))