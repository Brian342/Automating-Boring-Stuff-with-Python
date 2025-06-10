# The * (star or asterisk) means "Matching zero or more" - the group that
# precedes the star can occur any number of times in the text.
import re

batRegex = re.compile(r'Bat(wo)*man')
mo1 = batRegex.search('The adventures of Batman')
print(mo1.group())