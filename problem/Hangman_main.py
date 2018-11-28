"""Main"""
import Functions
word = input('what is your word? ').lower()
lettersLeft = list(word)
Functions.clear()

guessedLetters = []
correct = False
while not correct:
    print(Functions.board(word, guessedLetters))
    guessedLetters.append(Functions.guess())
    correct = Functions.checkCorrect(word, guessedLetters)


print(Functions.board(word, guessedLetters))
print('******YAY******')
