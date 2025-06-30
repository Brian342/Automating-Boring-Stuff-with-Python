import re

phoneRegex = re.compile(r'''(
(\d{3}|\(\d{3}\))? # area code
(\s| - |\.) ? # separator
\d{3} # first 3 digits

)''')