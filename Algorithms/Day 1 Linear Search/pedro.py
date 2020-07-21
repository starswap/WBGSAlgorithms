#Linear Search with file reading extension - Pedro
def linSearch(target, things): # The same linear search as in the js program
  for counter in range(0, len(things)):
    if target == things[counter]:
      print('found')
      break
    elif counter == len(things)-1:
      print('The thing you\'re looking for isn\'t in the list')

wordBank = open('words', 'rt') # Opens the file
wordList = wordBank.read().splitlines() # Reads into an array without the \ns
goal = input('What\'s your target? ')
wordBank.close() # Closes the file
linSearch(goal, wordList) 
