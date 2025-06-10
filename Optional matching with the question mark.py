import re

# batRegex = re.compile(r'Bat(wo)?man')
# mo1 = batRegex.search('The adventures of Batman')
# print(mo1.group())
#
# mo2 = batRegex.search('The adventures of Batwoman')
# print(mo2.group())

# searching text having an Area code or not
phoneRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
mo1 = phoneRegex.search('My Number is 415-555-4242')
print(mo1.group())

mo2 = phoneRegex.search('My number is 555-4242')
print(mo2.group())

# ? says Matching zero or one of the group preceding the question mark
