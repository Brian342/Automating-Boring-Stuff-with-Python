import re

# phoneNumberRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
# mo = phoneNumberRegex.search('My number is 415-555-4242.')
# # print(mo.group(1))
# # print(mo.group(2))
# # print(mo.group(0))
#
# # retrieving all groups at once
# # print(mo.groups())
#
# areaCode, phoneNumber = mo.groups()
# print(areaCode)
# print(phoneNumber)

phoneNumberRegex = re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)')
mo = phoneNumberRegex.search('My phone number is 415-555-4242')
mo.groups()

