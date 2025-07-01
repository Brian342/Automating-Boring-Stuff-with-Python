# step 1: create a regex for phone number

import pyperclip, re

phoneRegex = re.compile(r'''(
(\d{3}|\(\d{3}\))? # area code
(\s|-|\.) ? # separator
\d{3} # first 3 digits
(\s|-|\.) # separator
\d{4} # last 4 digit
(\s*(ext |x| ext.)\s*\d{2, 5})? # extension
)''', re.VERBOSE)

# step 2: create a regex for email addresses
emailRegex = re.compile(r'''(
[a-zA-Z0-9._%+-]+ # username
@ # @ symbol
[a-zA-z0-9-]+ # domain name
(\.[a-zA-Z]{2, 4}) # dot-something
)''', re.VERBOSE)

# step3: find all matches in the clipboard text
text = str(pyperclip.paste())
matches = []
for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        phoneNum += ' x' + groups[8]
    matches.append(phoneNum)
for groups in emailRegex.findall(text):
    matches.append(groups[0])

# step4: joins the matches into a string for the clipboard
# copy result to the clipboard
if len(matches) > 0:
    pass
