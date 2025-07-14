# step 1: Store the quiz data in a Dictionary
import random

# The quiz data. Keys are states and values are their capitals
capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'phoenix,',
            'Arkansas': 'Little Rocks', 'California': 'Sacramento', 'Colorado': 'Denver',
            'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee', 'Georgia': 'Atlanta',
            'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois': 'Springfield', 'Indiana': 'indianapolis',
            'Iowa': 'Des Moines', 'Kansas': 'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge',
            'Maine': 'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan': 'Lansing',
            'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri': 'Jefferson City', 'Montana': 'Helena',
            'Nebraska': 'Lincoln', 'Nevada': 'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton',
            'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh', 'North Dakota': 'Bismarck',
            'ohio': 'Columbus', 'Oklahoma': 'Oklahoma City', 'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg',
            'Rhode Island': 'Providence', 'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee': 'Nashville',
            'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont': 'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia',
            'West Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

# step2: create the quiz File and Shuffle the question order
# Generate 35 quiz files
for quizNum in range(35):
    # Create the quiz and answer key files
    quizFile = open('Capitals quiz%s.txt' % (quizNum + 1), 'w')
    answerKeyFile = open('Capitals quiz_answers%s.txt' % (quizNum + 1), 'w')

    # write out the header for the quiz
    quizFile.write('Name:\n\nDate:\n\nPeriod:\n\n')
    quizFile.write(('  ' * 20) + 'State Capitals quiz (form %s)' % (quizNum + 1))
    quizFile.write('\n\n')

    # shuffle the order of the state
    states = list(capitals.keys())
    random.shuffle(states)

# step3: Create the answer options
# loop through all 50 states, making a question for each.
for questionNum in range(50):
    # get right and wrong answers
    correctAnswers = capitals[states[questionNum]]
    wrongAnswers = list(capitals.values())
    del wrongAnswers[wrongAnswers.index(correctAnswers)]
    wrongAnswers = random.sample(wrongAnswers, 3)
    answerOptions = wrongAnswers + [correctAnswers]
    random.shuffle(answerOptions)

# step4: write content to the quiz and answer key files
# write the question and the answer options to the quiz file
quizFile.write('%s. what is the capital of %s?\n' % (questionNum + states[questionNum]))

for i in range (4):
    quizFile.write(' %s. %s\n' % ('ABCD'[i], answerOptions[i]))
quizFile.write('\n')
# write the answer key to a file
answerKeyFile.write('%s. %s\n' % (questionNum + 1, 'ABCD'[answerOptions.index]))



