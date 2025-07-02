# step 1: create a regex for phone number

import pyperclip, re

phoneRegex = re.compile(r'''
(
    (\d{3}|\(\d{3}\))?             # area code
    (\s|-|\.)?                     # separator
    (\d{3})                        # first 3 digits
    (\s|-|\.)                      # separator
    (\d{4})                        # last 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))? # extension
)
''', re.VERBOSE)

# Step 2: Regex for emails
emailRegex = re.compile(r'''
(
    [a-zA-Z0-9._%+-]+       # username
    @
    [a-zA-Z0-9.-]+          # domain name
    (\.[a-zA-Z]{2,})        # dot-something
)
''', re.VERBOSE)

# Step 3: Get text and find matches
text = str(pyperclip.paste())
matches = []

for groups in phoneRegex.findall(text):
    phoneNum = ''
    if groups[1]:  # area code
        phoneNum += groups[1] + '-'
    phoneNum += groups[3] + '-' + groups[5]
    if groups[8]:  # extension digits
        phoneNum += ' x' + groups[8]
    matches.append(phoneNum)

for groups in emailRegex.findall(text):
    matches.append(groups[0])

# Step 4: Copy results to clipboard
if matches:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No phone number or email found.')

