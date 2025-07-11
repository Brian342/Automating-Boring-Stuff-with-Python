import pprint
import mycats

# cats = [{'name': 'zophie', 'desc': 'chubby'}, {'name': 'pooka', 'desc': 'fluffy'}]
# print(pprint.pformat(cats))
#
# fileObj = open('mycats.py', 'w')
# print(fileObj.write('cats = ' + pprint.pformat(cats) + '\n'))
# fileObj.close()

print(mycats.cats)
print(mycats.cats[0])
print(mycats.cats[0]['name'])