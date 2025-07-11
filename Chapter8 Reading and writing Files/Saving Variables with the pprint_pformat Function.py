import pprint

cats = [{'name': 'zophie', 'desc': 'chubby'}, {'name': 'pooka', 'desc': 'fluffy'}]
print(pprint.pformat(cats))

fileObj = open('mycats.py', 'w')
print(fileObj.write('cats = ' + pprint.pformat(cats) + '\n'))
