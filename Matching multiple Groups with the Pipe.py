import re
# this character | is called Pipe used in matching one of many expressions

heroRegex = re.compile(r'Batman | Tina Fey', re.IGNORECASE)
# mo1 = heroRegex.search('Batman and Tina Fey')
# print(mo1.group())


heroRegex2 = re.compile('Tina Fey | Batman', re.IGNORECASE)
mo2 = heroRegex2.search('Tina Fey and Batman')

print(mo2.group())
