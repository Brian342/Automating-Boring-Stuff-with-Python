import pprint

cats = [{'name': 'zophie', 'desc': 'chubby'}, {'name': 'pooka', 'desc': 'fluffy'}]
print(pprint.pformat(cats))

fileObj = open('mycats.py', 'w')
fileObj.write('cats = ' + pprint.pformat(cats) + '\n')
