import re
# this character | is called Pipe used in matching one of many expressions

heroRegex = re.compile(r'Batman | Tina Fey')
# mo1 = heroRegex.search('Batman and Tina Fey')

# print(mo1.group())

mo2 = heroRegex.search('Tina Fey and Batman')

print(mo2.group())
