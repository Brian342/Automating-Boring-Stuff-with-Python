baconFile = open('bacon.txt', 'w')
print(baconFile.write('Hello world!\n'))

baconFile.close()
baconFile = open('bacon.txt', 'a')
baconFile.write('Bacon is not a vegetables')