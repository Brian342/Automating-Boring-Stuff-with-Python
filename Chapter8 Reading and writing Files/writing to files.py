baconFile = open('bacon.txt', 'w')
print(baconFile.write('Hello world!\n'))

baconFile.close()
baconFile = open('bacon.txt', 'a')
print(baconFile.write('Bacon is not a vegetables'))

baconFile.close()
baconFile = open('bacon.txt')
content = baconFile.read()
baconFile.close()
print(content)