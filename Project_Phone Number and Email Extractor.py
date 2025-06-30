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
)''')
