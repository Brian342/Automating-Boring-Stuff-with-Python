import re

namesRegex = re.compile(r'Agent \w+')
# print(namesRegex.sub('CENSORED', 'Agent Alice gave the secret documents to Agent Bob'))

# Names censor
agentNameRegex = re.compile(r'Agent (\w)\w*')
print(agentNameRegex.sub(r'\1****', 'Agent Alice told Agent'))